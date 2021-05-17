import scrapy
from museum.items import educationItem

class Education101Spider(scrapy.Spider):
    name = 'education101'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.qdyzyzmuseum.com/Home/Yanjiu/index/cateid/31']

    def parse_detail(self, response):
        item = response.meta["item"]
        if response.xpath('/html/body/div[5]/div/div/div[2]/h3/text()'):
            edu_name = response.xpath('/html/body/div[5]/div/div/div[2]/h3/text()').extract_first()
            print(edu_name)
        if response.xpath('/html/body/div[5]/div/div/div[2]/div/div/p/img/@src'):
            edu_img = 'http://www.qdyzyzmuseum.com' + response.xpath('/html/body/div[5]/div/div/div[2]/div/div/p/img/@src').extract_first()
            print(edu_img)
        #/html/body/div/div[1]/div[3]/div/div[2]/div[3]/div
        if response.xpath('/html/body/div[5]/div/div/div[2]/div/div/p//text()'):
            edu_desc = response.xpath('/html/body/div[5]/div/div/div[2]/div/div/p//text()').extract()
            edu_desc = ''.join(edu_desc)
            print(edu_desc)  

    def parse(self, response):
        item = educationItem()
        
        edu_list = response.xpath('/html/body/div[5]/div/div/div[2]/div')
        for div in edu_list:
            #/a[1]
            if div.xpath('./a[1]/@href'):
                detail_url = 'http://www.qdyzyzmuseum.com' +  div.xpath('./a[1]/@href').extract_first()           
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
