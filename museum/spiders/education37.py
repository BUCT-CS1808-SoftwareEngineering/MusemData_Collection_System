# 不可爬
import scrapy


class Education37Spider(scrapy.Spider):
    name = 'education37'
    allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xxx.com/']

    def parse(self, response):
        pass
