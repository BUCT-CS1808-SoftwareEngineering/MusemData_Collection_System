import scrapy


class Education159Spider(scrapy.Spider):
    name = 'education159'
    allowed_domains = ['www.ccc.com']
    start_urls = ['http://www.ccc.com/']

    def parse(self, response):
        pass
