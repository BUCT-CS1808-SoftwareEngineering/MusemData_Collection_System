import scrapy
from museum.items import collectionItem
import json


class Collection64Spider(scrapy.Spider):
    name = 'collection64'
    url = "http://www.guilinmuseum.org.cn/Collection/List/sh?page="
    
    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        'Content-Length': '0',
        "Connection": "keep-alive"
    }

    def start_requests(self):
        for i in range(1,4):
            yield scrapy.Request(self.url+f"{i}", headers=self.headers ,callback=self.parse)

    def parse(self, response):
        item = collectionItem()
        img_list = response.xpath(
            "//ul[@class='collectlist']/li//img/@src").getall()
        title_list = response.xpath(
            "//ul[@class='collectlist']/li//a/@title").getall()
        for index, i in enumerate(img_list):
            collectionName = title_list[index]
            collectionDescription = "无介绍"
            collectionImageUrl = i
            print((collectionName, collectionImageUrl,  collectionDescription))
        
