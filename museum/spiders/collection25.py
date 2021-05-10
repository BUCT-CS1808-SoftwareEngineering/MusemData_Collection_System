import scrapy
from museum.items import collectionItem
import re
# scrapy crawl collection25

class Collection25Spider(scrapy.Spider):
    name = 'collection25'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.cdmuseum.com/xianqin/',
    'https://www.cdmuseum.com/lianghan/',
    'https://www.cdmuseum.com/tangsong/',
    'https://www.cdmuseum.com/mq/',
    'https://www.cdmuseum.com/jinshi/',
    'https://www.cdmuseum.com/ms/',
    'https://www.cdmuseum.com/piying/',
    'https://www.cdmuseum.com/muou/',
    'https://www.cdmuseum.com/juanzeng/']

    def parse_detail(self, response):
        item = response.meta["item"]
        coll_name = response.xpath('/html/body/div[3]/div[1]/div[2]/div/div[1]/p[2]/text()').extract_first()
        print(coll_name)
        coll_img = response.xpath('/html/body/div[3]/div[1]/div[2]/div/div[2]/div//img/@src').extract_first()
        coll_img = 'https://www.cdmuseum.com' + coll_img
        print(coll_img)
        # if response.xpath('//*[@id="intro"]//text()'):
        coll_desc = response.xpath('/html/body/div[3]/div[1]/div[2]/div/div[2]/div//text()').extract()
        coll_desc = ''.join(coll_desc)
        print(coll_desc)
            
        # yield item

    def parse(self, response):
        item = collectionItem()
        coll_list = response.xpath('/html/body/div[3]/div[2]/div/div[2]/ul/li')
        for li in coll_list:
            detail_url = "https://www.cdmuseum.com" + li.xpath('./a/@href').extract_first()
            # print(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
