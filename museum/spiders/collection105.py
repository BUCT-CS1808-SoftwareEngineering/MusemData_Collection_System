import scrapy
from museum.items import collectionItem

class Collection105Spider(scrapy.Spider):
    name = 'collection105'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.kzbwg.cn/diancang/zhenpin/jj/']

    def parse_detail(self, response):
        item = response.meta["item"]
         
        if response.xpath('/html/body/div[6]/div/div/div[2]/div[2]/p//text()'):
            coll_desc = response.xpath('/html/body/div[6]/div/div/div[2]/div[2]/p//text()').extract()
            coll_desc = ''.join(coll_desc)
            print(coll_desc)  

    def parse(self, response):
        item = collectionItem()  
        coll_list = response.xpath('/html/body/div[6]/div/div/div[2]/div')
        #coll_name = response.xpath('/html/body/div[6]/div/div/div[2]/div[2]/div/h3/a/text()').extract_first()
        #print(coll_name)
        for div in coll_list:
            #detail_url = '1' 
            coll_name = div.xpath('./div/h3/a//text()').extract()
            coll_name = ''.join(coll_name)
            print(coll_name) 
            if div.xpath('./a/img/@src'):
                coll_img = div.xpath('./a/img/@src').extract_first()
                coll_img = 'http://www.kzbwg.cn' + coll_img
                print(coll_img)
            if div.xpath('./a/@href'):
                detail_url = 'http://www.kzbwg.cn' + div.xpath('./a/@href').extract_first()
                yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
            #yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
