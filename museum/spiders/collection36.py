import scrapy
from selenium import webdriver
from museum.items import collectionItem
import json
# scrapy crawl collection36

class Collection36Spider(scrapy.Spider):
    name = 'collection36'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.tssbwg.com.cn/html/guancang/']
    new_urls = ['http://www.tssbwg.com.cn/html/guancang/']
    deep_urls = []
    # url = 'http://www.zhejiangmuseum.com/Collection/ExcellentCollection?page=%d'
    # page_num = 2

    #实例化一个
    def __init__(self):
        self.bro = webdriver.Firefox()
        self.brom = webdriver.Firefox()

    def parse_detail(self, response):
        item = response.meta["item"]
        # if response.xpath('//*[@id="intro"]//text()'):
        coll_desc = '暂无'
        if response.xpath('//*[@id="Article"]/div[5]//text()').extract():
            coll_desc = response.xpath('//*[@id="Article"]/div[5]//text()').extract()
            coll_desc = ''.join(coll_desc)
        print(coll_desc)
            

    def parse(self, response):
        item = collectionItem()
        coll_list = response.xpath('//*[@id="layout"]/ul/li')
        # print (coll_list)
        for li in coll_list:
            # if li.xpath('./h3/a/text()').extract_first():
            name = li.xpath('./table/tbody/tr[2]/td/span/text()').extract_first()
            print(name)
            img = li.xpath('./table/tbody/tr[1]/td/a/img/@src').extract_first()
            print(img)
            detail_url = li.xpath('./table/tbody/tr[1]/td/a/@href').extract_first()
            print(detail_url)
            self.deep_urls.append(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})

    def closed(self,spider):
        self.bro.quit()
        self.brom.quit()
