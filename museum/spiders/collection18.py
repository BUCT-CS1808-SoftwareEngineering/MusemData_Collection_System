import scrapy
from selenium import webdriver
from museum.items import educationItem
import json
# scrapy crawl collection18

class Collection18Spider(scrapy.Spider):
    name = 'collection18'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.pgm.org.cn/pgm/wwls/201808/e2c2009345064fd7af7537aeb469ae0e.shtml']

    def parse(self, response):
        title = response.xpath('/html/body/div/div[2]/div/div[2]/div[2]/text()').extract_first()
        cont = response.xpath('//*[@id="content"]//text()').extract()
        cont = ''.join(cont)
        cont = title + "\n" + cont 
        print(cont)
