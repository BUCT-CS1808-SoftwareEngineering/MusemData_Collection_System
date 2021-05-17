import scrapy


class Education141Spider(scrapy.Spider):
    name = 'education141'
    allowed_domains = ['www.ccc.com']
    start_urls = ['http://www.ccc.com/']

    def parse(self, response):
        pass
