# -*- coding: utf-8 -*-
import scrapy
from museum.items import collectionItem


class Collection186Spider(scrapy.Spider):
    name = 'collection186'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xbpjng.cn/wenbotiandi/shuhua.aspx']
    next_url = 'http://www.xbpjng.cn/wenbotiandi/shuhua.aspx?page=%d'
    page_num = 2

    def parse(self, response):
        li_list = response.xpath('//ul[@class="piclist"]/li')
        for li in li_list:
            item = collectionItem()
            collectionImage = li.xpath('./a/img/@src').extract_first()
            if collectionImage[-1] != 'g':
                collectionImage = None
            # print(collectionImage)
            item['collectionImage'] = collectionImage
            collectionName = li.xpath('./a/h2/text()').extract_first()
            # print(collectionName)
            item['collectionName'] = collectionName
            url = 'http://www.xbpjng.cn/wenbotiandi/' + li.xpath('./a/@href').extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc, meta={'item': item})
        if self.page_num <= 4:
            new_url = self.next_url % self.page_num
            self.page_num += 1
            yield scrapy.Request(new_url, callback=self.parse)

    def parse_desc(self, response):
        collectionIntroduction = response.xpath('//p[@class="suba"]//text()').extract()
        collectionIntroduction = ''.join(collectionIntroduction).strip()
        # print(collectionIntroduction)
        item = response.meta['item']
        item['collectionIntroduction'] = collectionIntroduction
