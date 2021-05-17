import scrapy
from museum.items import collectionItem

class Collection96Spider(scrapy.Spider):
    name = 'collection96'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.hnzzmuseum.com/collection5_list.html']

    def parse_detail(self, response):
        item = response.meta["item"]
        #/html/body/div[4]/ul/div[2]/li[2]/p    
        if response.xpath('/html/body/div[4]/ul/div[2]/li[2]/p//text()'):
            coll_desc = response.xpath('/html/body/div[4]/ul/div[2]/li[2]/p//text()').extract()
            coll_desc = ''.join(coll_desc)
            print(coll_desc)  

    def parse(self, response):
        item = collectionItem()  
        #//*[@id="da-thumbs"] 
        coll_list = response.xpath('//*[@id="da-thumbs"]/li')
       
        for li in coll_list:
            #/html/body/div[4]/ul/div[1]/ul/li[1]/a/div/p/span[1]
            coll_name = li.xpath('./a/div/p/span[1]/text()').extract_first()
            print(coll_name)

            #/html/body/div[4]/ul/div[1]/ul/li[1]/a/img
            coll_img = li.xpath('./a/img/@src').extract_first()
            coll_img = 'http://www.hnzzmuseum.com' + coll_img
            print(coll_img)

            detail_url = 'http://www.hnzzmuseum.com' + li.xpath('./a/@href').extract_first()

            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
