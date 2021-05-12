# 不可爬
import scrapy


class Exhibition37Spider(scrapy.Spider):
    name = 'exhibition37'
    allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xxx.com/']

    def parse(self, response):
        pass
