import scrapy
from museum.items import collectionItem
import re

class Collection81Spider(scrapy.Spider):
    name = 'collection81'
    #allowed_domains = ['www.xxx.com']#允许访问的域
    start_urls = ['http://61.187.53.122/list.aspx?id=8&lang=zh-CN&page=1']
    #http://61.187.53.122/list.aspx?id=8&lang=zh-CN&page=1
    url = 'http://61.187.53.122/list.aspx?id=8&lang=zh-CN&page=%d'
    page_num = 2

    def parse_detail(self, response):
        item = response.meta["item"]
        #//*[@id="divContent"]
        if response.xpath('//*[@id="divContent"]/p[2]//text()'):
            coll_desc = response.xpath('//*[@id="divContent"]/p[2]//text()').extract()
            coll_desc = ''.join(coll_desc)
            print(coll_desc)  

    def parse(self, response):
        item = collectionItem()
        coll_list = response.xpath('//*[@id="thumbnailUL"]/li')
        #//*[@id="thumbnailUL"]
        for li in coll_list:
            coll_name = li.xpath('./div[2]/p/text()').extract_first()
            print(coll_name)
            detail_url = 'http://61.187.53.122/' + li.xpath('./div[1]/a/@href').extract_first()
            coll_img = li.xpath('./div[1]/a/img/@data-url').extract_first()
            #http://61.187.53.122/
            coll_img = 'http://61.187.53.122' + coll_img
            print(coll_img)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        
        if self.page_num <= 14:
            new_url = (self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)

        

 
            
       

    
