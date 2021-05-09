import scrapy


class Exhibition125Spider(scrapy.Spider):
    name = 'exhibition125'
    allowed_domains = ['www.ccc.com']
    start_urls = ['http://www.ccc.com/']

    def parse(self, response):
        pass
