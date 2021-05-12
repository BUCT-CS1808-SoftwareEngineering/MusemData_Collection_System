import scrapy
from museum.items import exhibitionItem 
import re
import json
# scrapy crawl exhibition35

class Exhibition35Spider(scrapy.Spider):
    name = 'exhibition35'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.plsbwg.com/index.php?m=content&c=index&a=lists&catid=2']

    def parse(self, response):
        item = exhibitionItem()
        div_list = response.xpath('/html/body/div[3]/div/ul/li')
        for div in div_list:
            name = div.xpath('./h2/text()').extract_first()
            print(name)
            img = div.xpath('./a/img/@src').extract_first()
            # img = 'http://www.portmuseum.cn' + img
            print(img)
            cont = "暂无"
            if div.xpath('./a/p/text()').extract():
                cont = div.xpath('./a/p/text()').extract()
                cont = ''.join(cont)
            print(cont)
            # detail_url = "http://www.nxgybwg.com" + div.xpath('./dt/a/@href').extract_first()
            # cont = div.xpath('./div/div[2]/span/text()').extract_first()
            # print(cont)
            # yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
