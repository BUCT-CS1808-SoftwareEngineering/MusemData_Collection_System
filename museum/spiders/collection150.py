import scrapy


class Collection150Spider(scrapy.Spider):
    name = 'collection150'
    allowed_domains = ['www.ccc.com']
    start_urls = ['http://www.ccc.com/']

    def parse(self, response):
        pass
