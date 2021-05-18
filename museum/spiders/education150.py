import scrapy


class Education150Spider(scrapy.Spider):
    name = 'education150'
    allowed_domains = ['www.ccc.com']
    start_urls = ['http://www.ccc.com/']

    def parse(self, response):
        pass
