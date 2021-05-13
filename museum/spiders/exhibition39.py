import scrapy
from museum.items import exhibitionItem 
import re
import json
# scrapy crawl exhibition39

class Exhibition39Spider(scrapy.Spider):
    name = 'exhibition39'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.yagmjng.com/rsf/site/jinianguan/zhongdianjieshao/index.html']

    def parse(self, response):
        item = exhibitionItem()
        div_list = response.xpath('//*[@id="zcnr"]/ul/li')
        num = 1
        for div in div_list:
            if num > 3:
                    break
            num += 1
            name = div.xpath('./a/font/text()').extract_first()
            print(name)
            detail_url = "http://www.yagmjng.com" + div.xpath('./a/@href').extract_first()
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
    
    def parse_detail(self, response):
        item = response.meta["item"]
        img = response.xpath('//*[@id="zcnr"]/p//img/@src').extract_first()
        img = 'http://www.yagmjng.com' + img
        print(img)
        cont = "暂无"
        if response.xpath('//*[@id="zcnr"]/p/span//text()').extract():
            cont = response.xpath('//*[@id="zcnr"]/p/span//text()').extract()
            cont = ''.join(cont)
        print(cont)

