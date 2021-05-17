import scrapy
from museum.items import educationItem

class Education106Spider(scrapy.Spider):
    name = 'education106'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.jiningmuseum.com/list/article_list.do?channelId=213']

    def parse_detail(self, response):
        item = response.meta["item"]
        #/html/body/div[3]/div[3]/div[2]/p[17]/img
        if response.xpath('/html/body/div[3]/div[3]/div[2]/p[17]/img/@src'):
            edu_img = response.xpath('/html/body/div[3]/div[3]/div[2]/p[17]/img/@src').extract_first()
            edu_img = 'http://www.jiningmuseum.com' + edu_img
            print(edu_img)
        if response.xpath('/html/body/div[3]/div[3]/div[2]/p//text()'):
            edu_desc = response.xpath('/html/body/div[3]/div[3]/div[2]/p//text()').extract()
            edu_desc = ''.join(edu_desc)
            print(edu_desc)  

    def parse(self, response):
        item = educationItem()
        edu_list = response.xpath('/html/body/div[3]/div[2]/div[1]/ul/li')
       
        for li in edu_list:
            #/html/body/div[3]/div[2]/div[1]/ul/li[1]/a/div[2]/h3
            edu_name = li.xpath('./a/div[2]/h3/text()').extract_first()
            print(edu_name)
            detail_url = 'http://www.jiningmuseum.com' + li.xpath('./a/@href').extract_first()
            #/html/body/div[3]/div[2]/div[1]/ul/li[2]/a/div[1]/img
            
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
