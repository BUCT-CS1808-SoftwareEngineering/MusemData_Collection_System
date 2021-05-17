import scrapy
from museum.items import collectionItem
#动态加载
class Collection92Spider(scrapy.Spider):
    name = 'collection92'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.wzbwg.com/news/52#']

    def parse(self, response):
        item = collectionItem()
        coll_name = response.xpath('/html/body/div[1]/div[13]/div/div/div[2]/div[2]/div/div[1]/div/p[1]/text()').extract_first()
        print(coll_name)
