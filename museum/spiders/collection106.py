import scrapy
from museum.items import collectionItem

class Collection106Spider(scrapy.Spider):
    name = 'collection106'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.jiningmuseum.com/collection_list.do?leibie=%E6%BC%86%E5%99%A8']

    def parse_detail(self, response):
        item = response.meta["item"]
        
        if response.xpath('/html/body/div[3]/div[3]/div[2]/ul/li[1]/a/img/@src'):
            coll_img = response.xpath('/html/body/div[3]/div[3]/div[2]/ul/li[1]/a/img/@src').extract_first()
            
            #coll_img = 'http://jzmsm.org' + coll_img
            print(coll_img)

    def parse(self, response):
        item = collectionItem()
        coll_list = response.xpath('/html/body/div[3]/div[3]/div[2]/div[1]/table/tbody/tr')
        
        for li in coll_list:
            
            coll_desc = li.xpath('./td//text()').extract()
            coll_desc = ''.join(coll_desc)
            print(coll_desc)

            #/html/body/div[3]/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[5]/a
            detail_url = 'http://www.jiningmuseum.com' + li.xpath('./td[5]/a/@href').extract_first()
            
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
