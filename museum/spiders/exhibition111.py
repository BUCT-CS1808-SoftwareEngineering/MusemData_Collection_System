import scrapy
from museum.items import exhibitionItem

class Exhibition111Spider(scrapy.Spider):
    name = 'exhibition111'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.wfsbwg.com/list/?53_1.html']

    def parse_detail(self, response):
        item = response.meta["item"]
        
        if response.xpath('/html/body/div[7]/div[2]/div[2]/div[2]/div[1]/div/p//text()'):
            exhib_desc = response.xpath('/html/body/div[7]/div[2]/div[2]/div[2]/div[1]/div/p//text()').extract()
            exhib_desc = ''.join(exhib_desc)
            print(exhib_desc)  
            

    def parse(self, response):
        item = exhibitionItem()
       
        exhib_list = response.xpath('/html/body/div[7]/div[2]/div[2]/div[1]/ul/li')
        
        for li in exhib_list:
            #/html/body/div[7]/div[2]/div[2]/div[1]/ul/li[1]/a
            exhib_name = li.xpath('./a/text()').extract_first()
            print(exhib_name)
            #/html/body/div[7]/div[2]/div[2]/div[1]/ul/li[1]/div/a/img
            exhib_img = li.xpath('./div/a/img/@src').extract_first()
            exhib_img = 'http://www.wfsbwg.com' + exhib_img
            print(exhib_img)
            detail_url = 'http://www.wfsbwg.com' + li.xpath('./div/a/@href').extract_first()
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
