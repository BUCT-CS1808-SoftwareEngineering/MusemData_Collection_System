import scrapy
from museum.items import collectionItem
#详情页介绍的url并不一致 循环用处不大
class Collection85Spider(scrapy.Spider):
    name = 'collection85'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.whgmbwg.com/gzjx/wwjc/index.shtml']
    
    def parse_detail(self, response):
        item = response.meta["item"]
        if response.xpath('/html/body/div[3]/div[5]/div/div[2]/div/div/p//text()|/html/body/div[3]/div[5]/div/div[2]/div/div[1]/div/p/br[3]//text()'):
            #/html/body/div[3]/div[5]/div/div[2]/div/div/p/span
            #/html/body/div[3]/div[5]/div/div[2]/div/div/p
            coll_desc = response.xpath('/html/body/div[3]/div[5]/div/div[2]/div/div/p//text()|/html/body/div[3]/div[5]/div/div[2]/div/div[1]/div/p/br[3]//text()').extract()
            coll_desc = ''.join(coll_desc)
            
            print(coll_desc)
          
        

    def parse(self, response):
        item = collectionItem()
        coll_list = response.xpath('/html/body/div[3]/div[5]/div[1]/ul/li')
        for li in coll_list:
           
            coll_name = li.xpath('./div/a/text()').extract_first()            
            print(coll_name)       
            detail_url = 'http://www.whgmbwg.com' + li.xpath('./a/@href').extract_first()
            coll_img = li.xpath('./a/img/@src').extract_first()
            coll_img = 'http://www.whgmbwg.com' + coll_img
            print(coll_img)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        
        
