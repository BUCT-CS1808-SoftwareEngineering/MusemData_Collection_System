import scrapy
from museum.items import collectionItem
#页面动态加载
class Collection110Spider(scrapy.Spider):
    name = 'collection110'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.jnmuseum.com/#/collection/list?type=CQ']

    def parse(self, response):
        item = collectionItem()
        coll_name = response.xpath('/html/body/div/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/a/div/text()').extract_first()
        print(coll_name)
