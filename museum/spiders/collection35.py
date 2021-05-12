import scrapy
from selenium import webdriver
from museum.items import collectionItem
import json
# scrapy crawl collection35

class Collection35Spider(scrapy.Spider):
    name = 'collection35'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.plsbwg.com/index.php?m=content&c=index&a=lists&catid=70',
    'http://www.plsbwg.com/index.php?m=content&c=index&a=lists&catid=23',
    'http://www.plsbwg.com/index.php?m=content&c=index&a=lists&catid=22',
    'http://www.plsbwg.com/index.php?m=content&c=index&a=lists&catid=24',
    'http://www.plsbwg.com/index.php?m=content&c=index&a=lists&catid=25',
    'http://www.plsbwg.com/index.php?m=content&c=index&a=lists&catid=26',
    'http://www.plsbwg.com/index.php?m=content&c=index&a=lists&catid=27',
    'http://www.plsbwg.com/index.php?m=content&c=index&a=lists&catid=28',
    'http://www.plsbwg.com/index.php?m=content&c=index&a=lists&catid=29',
    'http://www.plsbwg.com/index.php?m=content&c=index&a=lists&catid=30',
    'http://www.plsbwg.com/index.php?m=content&c=index&a=lists&catid=59',
    'http://www.plsbwg.com/index.php?m=content&c=index&a=lists&catid=60',
    'http://www.plsbwg.com/index.php?m=content&c=index&a=lists&catid=61',
    'http://www.plsbwg.com/index.php?m=content&c=index&a=lists&catid=63',
    'http://www.plsbwg.com/index.php?m=content&c=index&a=lists&catid=64',
    'http://www.plsbwg.com/index.php?m=content&c=index&a=lists&catid=65',
    'http://www.plsbwg.com/index.php?m=content&c=index&a=lists&catid=66',
    'http://www.plsbwg.com/index.php?m=content&c=index&a=lists&catid=67']

    def parse_detail(self, response):
        item = response.meta["item"]
        # if response.xpath('//*[@id="intro"]//text()'):
        coll_desc = 'None'
        if response.xpath('/html/body/div[3]/div/div[1]/div/ul//text()').extract():
            coll_desc = response.xpath('/html/body/div[3]/div/div[1]/div/ul//text()').extract()
            coll_desc = ''.join(coll_desc)
        print(coll_desc)
            

    def parse(self, response):
        item = collectionItem()
        coll_list = response.xpath('/html/body/div[3]/div[2]/div[3]/ul/li')
        # print (coll_list)
        for li in coll_list:
            # if li.xpath('./h3/a/text()').extract_first():
            name = li.xpath('./a/p/text()').extract_first()
            print(name)
            img = li.xpath('./a/div/img/@src').extract_first()
            print(img)
            detail_url = li.xpath('./a/@href').extract_first()
            print(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
