import scrapy
from museum.items import exhibitionItem 
import re
import json
# scrapy crawl exhibition38

class Exhibition38Spider(scrapy.Spider):
    name = 'exhibition38'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.dtxsmuseum.com/news_pic_list.aspx?category_id=24']

    def parse(self, response):
        item = exhibitionItem()
        div_list = response.xpath('//*[@id="form1"]/div[4]/div[2]/ul/li')
        num = 1
        for div in div_list:
            if num > 6:
                    break
            num += 1
            name = div.xpath('./a/span[2]/text()').extract_first()
            print(name)
            img = div.xpath('./a/span[1]/img/@src').extract_first()
            img = 'http://www.dtxsmuseum.com' + img
            print(img)
            detail_url = "http://www.dtxsmuseum.com" + div.xpath('./a/@href').extract_first()
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
    
    def parse_detail(self, response):
        item = response.meta["item"]
        cont = response.xpath('//*[@id="form1"]/div[4]/div[2]/div[4]//text()').extract()
        cont = ''.join(cont)
        print(cont)
