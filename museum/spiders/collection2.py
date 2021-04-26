import scrapy


class Collection2Spider(scrapy.Spider):
    name = 'collection2'
    allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.chnmuseum.cn/cg/']

    def parse(self, response):
        museum_ID = 2
        museum_name = '中国国家博物馆'
        
