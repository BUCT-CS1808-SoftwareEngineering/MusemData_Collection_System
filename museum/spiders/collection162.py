# -*- coding: utf-8 -*-
import scrapy
from museum.items import collectionItem


class Collection162Spider(scrapy.Spider):
    name = 'collection162'
    # allowed_domains = ['http://www.luxunmuseum.cn//']
    start_urls = ['http://www.luxunmuseum.cn/cp/index.html']

    def parse(self, response):
        a_list = response.xpath('//div[@class="am-gallery-item"]/a')
        for a in a_list:
            item = collectionItem()
            collectionImage = a.xpath('./img/@src').extract_first()
            # print(collectionImage)
            item['collectionImage'] = collectionImage
            collectionName = a.xpath('./h3/text()').extract_first()
            # print(collectionName)
            item['collectionName'] = collectionName
            url = 'http://www.luxunmuseum.cn' + a.xpath('./@href').extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc, meta={'item': item})

    def parse_desc(self, response):
        collectionIntroduction = response.xpath('//div[@class="am-cf "]/p/text()').extract()
        collectionIntroduction = ''.join(collectionIntroduction)
        # print(collectionIntroduction)
        item = response.meta['item']
        item['collectionIntroduction'] = collectionIntroduction