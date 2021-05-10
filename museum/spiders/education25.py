import scrapy
from museum.items import educationItem
import re 
# scrapy crawl education25

class Education25Spider(scrapy.Spider):
    name = 'education25'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.cdmuseum.com/yuyue/']

    def parse(self, response):
        item = educationItem()
        li_list = response.xpath('/html/body/div[3]/div[3]/ul/li')
        for li in li_list:
            # item['exhibName'] = name          
            # item['exhibImg'] = img
            name = li.xpath('./a/div[2]/p[1]/text()').extract()
            name = ''.join(name)
            print(name)
            cont = li.xpath('./a/div[2]/p[2]/text()').extract()
            cont = ''.join(cont)
            loca = li.xpath('./a/div[2]/div/p[2]/text()').extract_first()
            time = li.xpath('./a/div[2]/div/p[3]/text()').extract_first()
            cont = "\n时间：" + time + " 地点：" + loca + cont
            print(cont)
            img = li.xpath('./a/div[1]/img/@src').extract_first()
            img = 'https://www.cdmuseum.com' + img
            print(img)
