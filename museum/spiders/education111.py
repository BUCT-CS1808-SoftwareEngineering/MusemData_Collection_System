import scrapy
from museum.items import educationItem

class Education111Spider(scrapy.Spider):
    name = 'education111'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.wfsbwg.com/list/?10_1.html']

    def parse_detail(self, response):
        item = response.meta["item"]
        #/html/body/div[3]/div[3]/div[2]/p[17]/img
        if response.xpath('/html/body/div[7]/div[2]/div[2]/div[2]/p[2]/span/img/@src'):
            edu_img = response.xpath('/html/body/div[7]/div[2]/div[2]/div[2]/p[2]/span/img/@src').extract_first()
            edu_img = 'http://www.wfsbwg.com' + edu_img
            print(edu_img)
                           #/html/body/div[7]/div[2]/div[2]/div[2]/p[5]/span
        if response.xpath('/html/body/div[7]/div[2]/div[2]/div[2]/p[1]/span//text()'):
            edu_desc = response.xpath('/html/body/div[7]/div[2]/div[2]/div[2]/p[1]/span//text()').extract()
            edu_desc = ''.join(edu_desc)
            print(edu_desc)  

    def parse(self, response):
        item = educationItem()
        edu_list = response.xpath('/html/body/div[7]/div[2]/div[2]/ul/li')
       
        for li in edu_list:
            #/html/body/div[7]/div[2]/div[2]/ul/li[1]/a
            edu_name = li.xpath('./a/text()').extract_first()
            print(edu_name)
            detail_url = 'http://www.wfsbwg.com' + li.xpath('./a/@href').extract_first()
            #/html/body/div[3]/div[2]/div[1]/ul/li[2]/a/div[1]/img
            
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
