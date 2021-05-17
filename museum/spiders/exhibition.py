import scrapy


class ExhibitionSpider(scrapy.Spider):
    name = 'exhibition'
    allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xxx.com/']

    def parse(self, response):
        pass
