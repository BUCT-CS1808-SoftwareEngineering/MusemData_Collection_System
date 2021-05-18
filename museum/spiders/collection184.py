# -*- coding: utf-8 -*-
import scrapy
from museum.items import collectionItem


class Collection184Spider(scrapy.Spider):
    name = 'collection184'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.balujun.cn/e/action/ShowInfo.php?classid=45&id=1683',
                  'http://www.balujun.cn/e/action/ShowInfo.php?classid=46&id=1705',
                  'http://www.balujun.cn/e/action/ShowInfo.php?classid=45&id=1680',
                  'http://www.balujun.cn/e/action/ShowInfo.php?classid=45&id=1681']

    def parse(self, response):
        item = collectionItem()
        collectionImage = response.xpath('//div[@class="v_news_content"]//img/@src').extract_first()
        if collectionImage != None:
            collectionImage = 'http://www.balujun.cn/' + collectionImage
        # print(collectionImage)
        item['collectionImage'] = collectionImage
        collectionName = response.xpath('//div[@class="content-title"]/h3/text()').extract_first().strip()
        # print(collectionName)
        item['collectionName'] = collectionName
        collectionIntroduction = response.xpath('//div[@class="v_news_content"]/p//text()').extract()
        collectionIntroduction = ''.join(collectionIntroduction).strip()
        # print(collectionIntroduction)
        item['collectionIntroduction'] = collectionIntroduction
