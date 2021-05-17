import scrapy
from museum.items import educationItem

class Education93Spider(scrapy.Spider):
    name = 'education93'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.aybwg.org/anbojiaoyu/']

    def parse_detail(self, response):
        item = response.meta["item"]
        edu_img = response.xpath('/html/body/div/div[4]/div[2]/div/div[2]/div[1]/img/@src').extract_first()
        print(edu_img)
        #/html/body/div/div[4]/div[2]/div/div[2]/div[1]/strong/span/span
        #/html/body/div/div[4]/div[2]/div/div[2]/p[1]/span[1]
        #/html/body/div/div[4]/div[2]/div/div[2]/p[2]/span[2]
        if response.xpath('/html/body/div/div[4]/div[2]/div/div[2]/p//text()'):
            edu_desc = response.xpath('//html/body/div/div[4]/div[2]/div/div[2]/p//text()').extract()
            edu_desc = ''.join(edu_desc)
            print(edu_desc)  

    def parse(self, response):
        item = educationItem()
        
        edu_list = response.xpath('/html/body/div/div[4]/div[2]/ul/li')
        
        for li in edu_list:
            #/html/body/div/div[4]/div[2]/ul/li[1]/a/p
            edu_name = li.xpath('./a/p/text()').extract_first()
            print(edu_name)
            #/div[1]/a
            detail_url = li.xpath('./a/@href').extract_first()
            #edu_img = li.xpath('./div[1]/a/img/@src').extract_first()
            #http://61.187.53.122/
            #edu_img = 'http://www.ycbwg.com' + edu_img
            #print(edu_img)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
