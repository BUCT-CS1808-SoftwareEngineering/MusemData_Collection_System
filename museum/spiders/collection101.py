import scrapy
from museum.items import collectionItem

class Collection101Spider(scrapy.Spider):
    name = 'collection101'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.qdyzyzmuseum.com/Home/Diancang/index/cateid/44']

    def parse_detail(self, response):
        item = response.meta["item"]
        if response.xpath('/html/body/div[5]/div/div/div[2]/div[1]/div[1]/h3//text()'):
            coll_name = response.xpath('/html/body/div[5]/div/div/div[2]/div[1]/div[1]/h3//text()').extract()
            coll_name = ''.join(coll_name)
            print(coll_name)  
        if response.xpath('/html/body/div[5]/div/div/div[2]/div[2]/div/p/img/@src'):
            coll_img = 'http://www.qdyzyzmuseum.com' + response.xpath('/html/body/div[5]/div/div/div[2]/div[2]/div/p/img/@src').extract_first()
            print(coll_img)

    def parse(self, response):
        item = collectionItem()  
        coll_list = response.xpath('/html/body/div[5]/div/div/div[2]/div')
       
        for div in coll_list:
            #detail_url = '1' 
            if div.xpath('./a/@href'):
                detail_url = 'http://www.qdyzyzmuseum.com' + div.xpath('./a/@href').extract_first()
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
