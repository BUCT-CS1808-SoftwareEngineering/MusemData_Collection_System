import scrapy


class Education145Spider(scrapy.Spider):
    name = 'education145'
    allowed_domains = ['www.ccc.com']
    start_urls = ['http://www.ccc.com/']

    def parse(self, response):
        pass
