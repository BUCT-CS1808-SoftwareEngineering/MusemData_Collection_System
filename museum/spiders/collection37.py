# 不可爬
import scrapy
from museum.items import collectionItem
import json
from selenium import webdriver
# scrapy crawl collection37

class Collection37Spider(scrapy.Spider):
    name = 'collection37'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://public.dha.ac.cn/list.aspx?ID=884355801619']

    new_urls = ['http://public.dha.ac.cn/list.aspx?ID=884355801619']
    # deep_urls = []
    url = 'http://public.dha.ac.cn/list.aspx?ID=884355801619&Page=%d'
    page_num = 2

    #实例化一个
    def __init__(self):
        self.bro = webdriver.Firefox()
        # self.brom = webdriver.Firefox()

    # def parse_detail(self, response):
    #     item = response.meta["item"]
    #     # if response.xpath('//*[@id="intro"]//text()'):
    #     coll_desc = '暂无'
    #     if response.xpath('//*[@id="Article"]/div[5]//text()').extract():
    #         coll_desc = response.xpath('//*[@id="Article"]/div[5]//text()').extract()
    #         coll_desc = ''.join(coll_desc)
    #     print(coll_desc)
            

    def parse(self, response):
        item = collectionItem()
        coll_list = response.xpath('/html/body/div[1]/div[4]/div[2]/div[2]/table[2]/tbody/tr')
        # print (coll_list)
        for li in coll_list:
            # if li.xpath('./h3/a/text()').extract_first():
            name = li.xpath('./td/div/div[2]/div[1]/a/text()').extract_first()
            print(name)
            img = li.xpath('./td/div/div[1]/a/img/@src').extract_first()
            print(img)
            cont = li.xpath('./td/div/div[2]/div[2]/text()').extract_first()
            # cont = ''.join()
            print(cont)
            # detail_url = li.xpath('./table/tbody/tr[1]/td/a/@href').extract_first()
            # print(detail_url)
            # self.deep_urls.append(detail_url)
            # yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        if self.page_num <= 7:
            new_url = (self.url%self.page_num)
            self.new_urls.append(new_url)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)

    def closed(self,spider):
        self.bro.quit()
        # self.brom.quit()
