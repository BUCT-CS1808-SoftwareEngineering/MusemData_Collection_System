import scrapy
from museum.items import collectionItem

class Collection91Spider(scrapy.Spider):
    name = 'collection91'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.pdsm.org.cn/front/collection/browsecollection.html?page=1']

    url = 'http://www.pdsm.org.cn/front/collection/browsecollection.html?page=%d'
    page_num = 2

      
    def parse(self, response):
        item = collectionItem()
        coll_list = response.xpath('/html/body/div[3]/div[4]/ul/li')
        
        for li in coll_list:
            #./div/p/a
            coll_name = li.xpath('./div/p/a/text()').extract_first()
            print(coll_name)
            #./div/span/a/img
            coll_img = li.xpath('./div/span/a/img/@src').extract_first()
            coll_img = 'http://www.pdsm.org.cn' + coll_img
            print(coll_img)
            #/div/span/a
            #藏品无描述
            #detail_url = 'http://61.187.53.122/' + li.xpath('./div/span/a/@href').extract_first()
            #yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        
        if self.page_num <= 10:
            new_url = (self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)
