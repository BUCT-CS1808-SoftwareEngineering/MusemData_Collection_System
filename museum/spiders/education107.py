import scrapy
from museum.items import educationItem

class Education107Spider(scrapy.Spider):
    name = 'education107'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.ytmuseum.com/academic/jd']
    url = 'http://www.ytmuseum.com/academic/jd?p=%d'
    page_num = 2
    def parse_detail(self, response):
        item = response.meta["item"]
        #/html/body/div[3]/div[3]/div[2]/p[17]/img
        if response.xpath('/html/body/div[3]/div[2]/div/div/div[4]/div[3]/p[1]/img/@src'):
            edu_img = response.xpath('/html/body/div[3]/div[2]/div/div/div[4]/div[3]/p[1]/img/@src').extract_first()
            #edu_img = 'http://www.jiningmuseum.com' + edu_img
            print(edu_img)
        if response.xpath('/html/body/div[3]/div[2]/div/div/div[4]/div[3]/p[3]/span/img/@src'):
            edu_desc = response.xpath('/html/body/div[3]/div[2]/div/div/div[4]/div[3]/p[3]/span/img/@src').extract_first()
            #edu_desc = ''.join(edu_desc)
            print(edu_desc)  

    def parse(self, response):
        item = educationItem()
        edu_list = response.xpath('/html/body/div[3]/div[2]/div[1]/div/div/div[4]/div/div[1]/div')
       
        for li in edu_list:
            #/html/body/div[3]/div[2]/div[1]/div/div/div[4]/div/div[1]/div[1]/a
            edu_name = li.xpath('./a/text()').extract_first()
            print(edu_name)
            detail_url = 'http://www.ytmuseum.com' + li.xpath('./a/@href').extract_first()
            #/html/body/div[3]/div[2]/div[1]/ul/li[2]/a/div[1]/img
            
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        if self.page_num <= 2:
            new_url = (self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)