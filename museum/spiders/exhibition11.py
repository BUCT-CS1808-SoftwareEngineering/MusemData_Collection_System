# 动态加载+Ajax
import scrapy


class Exhibition11Spider(scrapy.Spider):
    name = 'exhibition11'
    allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xxx.com/']

    def parse(self, response):
        pass
