# -*- coding: utf-8 -*-
import scrapy
import json
from museum.items import collectionItem


class Collection187Spider(scrapy.Spider):
    name = 'collection187'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://api.bwy.hbdjdz.com:9903//primaryCollection/list4Page?id=1&relicsType=1&pageSize=10000']

    def parse(self, response):
        item = collectionItem()
        li_list = json.loads(response.text)['data']
        for li in li_list:
            collectionName = li['name']
            # print(collectionName)
            collectionIntroduction = li['introduce']
            # print(collectionIntroduction)
            collectionImage = li['imgPath']
            # print(collectionImage)
