import scrapy
from museum.items import educationItem
import re 
# scrapy crawl education27

class Education27Spider(scrapy.Spider):
    name = 'education27'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.portmuseum.cn/doc/jy/gbjt/index.shtml']

    def parse(self, response):
        item = educationItem()
        li_list = response.xpath('/html/body/div[3]/div[2]/ul/li')
        for li in li_list:
            # item['exhibName'] = name          
            # item['exhibImg'] = img
            name = li.xpath('./a/h3/text()').extract()
            name = ''.join(name)
            print(name)
            cont = li.xpath('./div/div/p/text()').extract()
            cont = ''.join(cont)
            # loca = li.xpath('./a/div[2]/div/p[2]/text()').extract_first()
            # time = li.xpath('./a/div[2]/div/p[3]/text()').extract_first()
            # cont = "\n时间：" + time + " 地点：" + loca + cont
            print(cont)
            img = li.xpath('./div/a/img/@src').extract_first()
            img = 'http://www.portmuseum.cn' + img
            print(img)
