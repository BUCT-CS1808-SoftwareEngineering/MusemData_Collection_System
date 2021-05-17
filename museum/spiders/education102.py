import scrapy
from museum.items import educationItem


class Education102Spider(scrapy.Spider):
    name = 'education102'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://museum.sdu.edu.cn/xszz.htm']
    
    
    def parse_detail(self, response):
        item = response.meta["item"]
        
        if response.xpath('/html/body/div[2]/div[2]/form/div[2]/div/p[4]//text()'):
            edu_desc = response.xpath('/html/body/div[2]/div[2]/form/div[2]/div/p[4]//text()').extract()
            edu_desc = ''.join(edu_desc)
            print(edu_desc)  

    def parse(self, response):
        item = educationItem()
        
        edu_list = response.xpath('//*[@id="c"]/div')
        for div in edu_list:
            
            edu_name = div.xpath('./div[3]/a/@title').extract_first()
            print(edu_name)           
            detail_url = 'http://museum.sdu.edu.cn/' + div.xpath('./div[3]/a/@href').extract_first()
            edu_img = 'http://museum.sdu.edu.cn' + div.xpath('./div[2]/a/img/@src').extract_first()
            print(edu_img)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        