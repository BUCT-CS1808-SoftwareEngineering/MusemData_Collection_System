import scrapy


class Education122Spider(scrapy.Spider):
    name = 'education122'
    allowed_domains = ['www.ccc.com']
    start_urls = ['http://www.ccc.com/']

    def parse(self, response):
        pass
