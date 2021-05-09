import scrapy


class Exhibition124Spider(scrapy.Spider):
    name = 'exhibition124'
    allowed_domains = ['www.ccc.con']
    start_urls = ['http://www.ccc.con/']

    def parse(self, response):
        pass
