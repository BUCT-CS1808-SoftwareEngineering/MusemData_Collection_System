import scrapy


class Collection100Spider(scrapy.Spider):
    name = 'collection100'
    allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xxx.com/']

    def parse(self, response):
        pass
