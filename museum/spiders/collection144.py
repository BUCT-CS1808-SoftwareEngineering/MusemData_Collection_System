import scrapy


class Collection144Spider(scrapy.Spider):
    name = 'collection144'
    allowed_domains = ['www.ccc.com']
    start_urls = ['http://www.ccc.com/']

    def parse(self, response):
        pass
