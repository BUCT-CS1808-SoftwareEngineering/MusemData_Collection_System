import scrapy


class Exhibition123Spider(scrapy.Spider):
    name = 'exhibition123'
    allowed_domains = ['www.ccc.com']
    start_urls = ['http://www.ccc.com/']

    def parse(self, response):
        pass
