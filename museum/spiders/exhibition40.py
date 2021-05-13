import scrapy
from museum.items import exhibitionItem 
import re
import json
# scrapy crawl exhibition40

class Exhibition40Spider(scrapy.Spider):
    name = 'exhibition40'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://bpmuseum.com/index.php?m=content&c=index&a=lists&catid=38']

    def parse(self, response):
        item = exhibitionItem()
        div_list = response.xpath('//*[@id="brand-waterfall"]/div')
        num = 1
        for div in div_list:
            if div.xpath('./div/div/h3/a/text()').extract_first():
                if num > 6:
                        break
                num += 1
                name = div.xpath('./div/div/h3/a/text()').extract_first()
                print(name)
                img = "https://bpmuseum.com/" + div.xpath('./div/a/img/@src').extract_first()
                print(img)
                cont = div.xpath('./div/div/p/a//text()').extract_first()
                print(cont)
            # detail_url = "http://www.yagmjng.com" + div.xpath('./a/@href').extract_first()
            # yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
    
