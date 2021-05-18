# -*- coding: utf-8 -*-
import scrapy
from museum.items import collectionItem


class Collection170Spider(scrapy.Spider):
    name = 'collection170'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://museum.nenu.edu.cn/info/1028/3502.htm']

    def parse(self, response):
        td_list = response.xpath('//tr[@class="firstRow"]/td')
        for td in td_list:
            item = collectionItem()
            collectionImage = td.xpath('.//img/@src').extract_first()
            if collectionImage != None:
                collectionImage = 'http://museum.nenu.edu.cn' + collectionImage
            # print(collectionImage)
            item['collectionImage'] = collectionImage
            collectionName = td.xpath('./ul/li[2]//text()').extract_first()
            # print(collectionName)
            item['collectionName'] = collectionName
            collectionIntroduction = collectionName
            # print(collectionIntroduction)
            item['collectionIntroduction'] = collectionIntroduction
