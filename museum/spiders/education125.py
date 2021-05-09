import scrapy


class Education125Spider(scrapy.Spider):
    name = 'education125'
    allowed_domains = ['www.ccc.com']
    start_urls = ['http://www.ccc.com/']

    def parse(self, response):
        pass
