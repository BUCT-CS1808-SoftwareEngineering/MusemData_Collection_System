import scrapy
from museum.items import collectionItem

class Collection95Spider(scrapy.Spider):
    name = 'collection95'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.eywsqsfbwg.com/index.php?m=content&c=index&a=lists&catid=15']


    def parse_detail(self, response):
        item = response.meta["item"]   
        #/html/body/div[4]/div[2]/div/div[1]/p 
        if response.xpath('/html/body/div[4]/div[2]/div/div[1]/p//text()'):
            coll_desc = response.xpath('/html/body/div[4]/div[2]/div/div[1]/p//text()').extract()
            coll_desc = ''.join(coll_desc)
            print(coll_desc)  

    def parse(self, response):
        item = collectionItem()   
        coll_list = response.xpath('/html/body/div[4]/div[2]/div[2]/ul/li')
        #/html/body/div[4]/div[2]/div[2]/ul
        #/html/body/div[4]/div[2]/div[2]
        for li in coll_list:
            #/html/body/div[4]/div[2]/div[2]/ul/li[1]/a/p
            coll_name = li.xpath('./a/p/text()').extract_first()
            print(coll_name)

            #/html/body/div[4]/ul/div[1]/ul/li[1]/a/img
            coll_img = li.xpath('./a/img/@src').extract_first()
            coll_img = 'http://www.eywsqsfbwg.com/' + coll_img
            print(coll_img)

            detail_url =  li.xpath('./a/@href').extract_first()

            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        
        
