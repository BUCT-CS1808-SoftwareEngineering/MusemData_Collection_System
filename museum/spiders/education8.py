#无教育


import scrapy


class Education8Spider(scrapy.Spider):
    name = 'education8'
    allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xxx.com/']

    def parse(self, response):
        pass
