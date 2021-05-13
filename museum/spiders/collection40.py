import scrapy
from museum.items import collectionItem
import re
import json
# scrapy crawl collection40

class Collection40Spider(scrapy.Spider):
    name = 'collection40'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://bpmuseum.com/index.php?m=content&c=index&a=lists&catid=19',
    'https://bpmuseum.com/index.php?m=content&c=index&a=lists&catid=20',
    'https://bpmuseum.com/index.php?m=content&c=index&a=lists&catid=21',
    'https://bpmuseum.com/index.php?m=content&c=index&a=lists&catid=40']

    def parse(self, response):
        item = collectionItem()
        div_list = response.xpath('//*[@id="brand-waterfall"]/div')
        for div in div_list:
            name = div.xpath('./div/div/h3/a/text()').extract_first()
            print(name)
            img = "https://bpmuseum.com" + div.xpath('./div/a/img/@src').extract_first()
            print(img)
            detail_url = "http://www.yagmjng.com" + div.xpath('./div/a/@href').extract_first()
            cont = "暂无"
            print(cont)
            # yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
    
    # def parse_detail(self, response):
    #     item = response.meta["item"]
    #     img = response.xpath('//*[@id="zcnr"]/p//img/@src').extract_first()
    #     img = 'http://www.yagmjng.com' + img
    #     print(img)
    #     cont = "暂无"
    #     if response.xpath('//*[@id="zcnr"]/p/span//text()').extract():
    #         cont = response.xpath('//*[@id="zcnr"]/p/span//text()').extract()
    #         cont = ''.join(cont)
    #     print(cont)
