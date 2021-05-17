import scrapy
from museum.items import educationItem

class Education100Spider(scrapy.Spider):
    name = 'education100'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.zbstcbwg.cn/education.html']

    def parse_detail(self, response):
        item = response.meta["item"]
        #/html/body/div/div[1]/div[3]/div/div[2]/div[3]/div
        if response.xpath('/html/body/div[3]/div/div/div[3]/blockquote//text()'):
            edu_desc = response.xpath('/html/body/div[3]/div/div/div[3]/blockquote//text()').extract()
            edu_desc = ''.join(edu_desc)
            print(edu_desc)  

    def parse(self, response):
        item = educationItem()
        
        edu_list = response.xpath('/html/body/div[3]/div[1]/div/div[4]/div[1]/div')
        for div in edu_list:
            
            edu_name = div.xpath('./a/div[2]/div[1]/text()').extract_first()
            print(edu_name)
            
            detail_url = '1' 
            if div.xpath('./a/@href'):
                detail_url = 'http://www.zbstcbwg.cn' +  div.xpath('./a/@href').extract_first()
                
            else:
                print('detail_url is null')
            
            edu_img = 'http://www.zbstcbwg.cn' + div.xpath('./a/div[1]/img/@src').extract_first()
            print(edu_img)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
    
