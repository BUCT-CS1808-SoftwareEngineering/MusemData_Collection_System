import scrapy
from museum.items import educationItem
import re 
import json
# scrapy crawl education39

class Education39Spider(scrapy.Spider):
    name = 'education39'
    start_urls = ['http://www.yagmjng.com/rsf/site/jinianguan/xuanjiaobolan/index.html']

    def parse(self, response):
        item = educationItem()
        li_list = response.xpath('//*[@id="zcnr"]/ul/li')
        num = 1
        for li in li_list:
            if num > 6:
                break
            name = li.xpath('./a/font/text()').extract_first()
            print(name)
            detail_url = "http://www.yagmjng.com" + li.xpath('./a/@href').extract_first()
            # print(detail_url)
            yield scrapy.Request(url=detail_url,callback=self.parse_detail,meta={'item':item})
    
    def parse_detail(self, response):
        item = response.meta["item"]
        img = "http://www.yagmjng.com" + response.xpath('//*[@id="zcnr"]/p//img/@src').extract_first()
        print(img)
        cont = response.xpath('//*[@id="zcnr"]/p//text()').extract()
        cont = ''.join(cont)
        # cont = re.sub('【\d】','',cont)
        print(cont)
