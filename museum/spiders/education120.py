import scrapy
from museum.items import educationItem

class Education120Spider(scrapy.Spider):
    name = 'education120'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.qingdaomuseum.com/education']
    url = 'http://www.qingdaomuseum.com/education/index/16/%d'
    page_num = 2
    
    def parse_detail(self, response):
        item = response.meta["item"]
        if response.xpath('/html/body/div[6]/div[2]/div/div[4]/p//text()'):
            edu_desc = response.xpath('/html/body/div[6]/div[2]/div/div[4]/p//text()').extract()
            edu_desc = ''.join(edu_desc)
            print(edu_desc)  
        #print("1")

    def parse(self, response):
        item = educationItem()
        
        edu_list = response.xpath('/html/body/div[6]/div[3]/div[3]/div[4]/div')
        for div in edu_list:
            edu_name = div.xpath('./div/div[2]/div/h4/a/text()').extract_first()
            print(edu_name)
            edu_img = div.xpath('./div/div[1]/div/a/img/@src').extract_first()
            #edu_img = 'http://museum.linyi.cn' + edu_img
            print(edu_img)
            detail_url = div.xpath('./div/div[1]/div/a/@href').extract_first()
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        if self.page_num <= 4:
            new_url = (self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)