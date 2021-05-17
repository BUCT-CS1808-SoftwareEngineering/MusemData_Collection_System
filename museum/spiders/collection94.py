import scrapy
from museum.items import collectionItem
#详情页信息为none
class Collection94Spider(scrapy.Spider):
    name = 'collection94'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.kfsbwg.com/html/wenwu/taoci/']


    def parse_detail(self, response):
        item = response.meta["item"]
        #/html/body/div[3]/div[2]/div/p[1]/br[3]
        #if response.xpath('/html/body/div[3]/div[2]/div/p[1]/br//text()'):
            #coll_desc = response.xpath('/html/body/div[3]/div[2]/div/p[1]/br//text()').extract()
            #coll_desc = ''.join(coll_desc)
            #print(coll_desc) 
        if response.xpath('/html/body/div[3]/div[2]/div/p[1]/strong[1]//text()'):
            coll_desc = response.xpath('/html/body/div[3]/div[2]/div/p[1]/strong[1]//text()').extract()
            coll_desc = ''.join(coll_desc)
            print(coll_desc)  
        #print("1")
        #http://www.kfsbwg.com/html/2016/taoci_0815/101.html
        #http://www.kfsbwg.com/html/2016/taoci_0815/101.html

    def parse(self, response):
        item = collectionItem()
        coll_list = response.xpath('/html/body/div[2]/div[2]/ul/li')
        
        for li in coll_list:
            #/html/body/div[2]/div[2]/ul/li[1]/p/a
            coll_name = li.xpath('./p/a/text()').extract_first()
            print(coll_name)
            detail_url = li.xpath('./a/@href').extract_first()
            coll_img = li.xpath('./a/img/@src').extract_first()
            print(coll_img)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
