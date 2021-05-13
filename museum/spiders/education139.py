import scrapy


class Education139Spider(scrapy.Spider):
    name = 'education139'
    allowed_domains = ['www.ccc.com']
    start_urls = ['http://www.ccc.com/']

    def parse(self, response):
        pass
