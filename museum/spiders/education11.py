# 动态加载+Ajax
import scrapy


class Education11Spider(scrapy.Spider):
    name = 'education11'
    allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xxx.com/']

    def parse(self, response):
        pass
