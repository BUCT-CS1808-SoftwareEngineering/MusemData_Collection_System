# 无藏品
import scrapy


class Collection13Spider(scrapy.Spider):
    name = 'collection13'
    allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xxx.com/']

    def parse(self, response):
        pass
