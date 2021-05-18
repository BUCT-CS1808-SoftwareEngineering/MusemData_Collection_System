# -*- coding: utf-8 -*-
import scrapy
from museum.items import collectionItem


class Collection183Spider(scrapy.Spider):
    name = 'collection183'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.coalmus.org.cn/html/list_1556.html',
                  'http://www.coalmus.org.cn/html/list_1557.html',
                  'http://www.coalmus.org.cn/html/list_1558.html',
                  'http://www.coalmus.org.cn/html/list_1559.html',
                  'http://www.coalmus.org.cn/html/list_1560.html',
                  'http://www.coalmus.org.cn/html/list_1560_1.html',
                  'http://www.coalmus.org.cn/html/list_1561.html',
                  'http://www.coalmus.org.cn/html/list_1562.html',
                  'http://www.coalmus.org.cn/html/list_1562_1.html'
                  ]

    def parse(self, response):
        li_list = response.xpath('//div[@class="piclistbox"]/ul/li')
        for li in li_list:
            item = collectionItem()
            collectionImage = li.xpath('./div[1]/a/img/@src').extract_first()
            # print(collectionImage)
            item['collectionImage'] = collectionImage
            collectionName = li.xpath('./div[2]/a/text()').extract_first()
            # print(collectionName)
            item['collectionName'] = collectionName
            url = li.xpath('./div[2]/a/@href').extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc, meta={'item': item})

    def parse_desc(self, response):
        collectionIntroduction = response.xpath('//div[@class="nph_intro"]//text()').extract()
        collectionIntroduction = ''.join(collectionIntroduction).strip()
        # print(response.url, collectionIntroduction)
        item = response.meta['item']
        item['collectionIntroduction'] = collectionIntroduction
