import scrapy
from museum.items import educationItem
import re 
# scrapy crawl education32

class Education32Spider(scrapy.Spider):
    name = 'education32'
    start_urls = ['http://www.nxbwg.com/c/xcjy.html']

    def parse(self, response):
        item = educationItem()
        div_list = response.xpath('//*[@id="content-container"]/div[2]/div[2]/main/div/div/div/article')
        for div in div_list:
            name = div.xpath('./div[1]/h3/a/text()').extract_first()
            print(name)
            img = div.xpath('./div[2]/div[1]/img/@src').extract_first()
            # img = 'http://www.portmuseum.cn' + img
            print(img)
            cont = div.xpath('./div[2]/div[2]//text()').extract()
            cont = ''.join(cont)
            # cont = div.xpath('./div/div[2]/span/text()').extract_first()
            print(cont)
