import scrapy


class Education152Spider(scrapy.Spider):
    name = 'education152'
    allowed_domains = ['www.ccc.com']
    start_urls = ['http://www.ccc.com/']

    def parse(self, response):
        pass
