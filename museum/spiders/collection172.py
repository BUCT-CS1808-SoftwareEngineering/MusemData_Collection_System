# -*- coding: utf-8 -*-
import scrapy
from museum.items import collectionItem


class Collection172Spider(scrapy.Spider):
    name = 'collection172'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.dlnm.org.cn/?_f=boutique']
    next_url = 'http://www.dlnm.org.cn/?_f=boutique&p=%d'
    page_num = 2

    def parse(self, response):
        li_list = response.xpath('//ul[@class="themelist"]/li')
        for li in li_list:
            item = collectionItem()
            collectionImage = li.xpath('./a/img/@src').extract_first()
            # print(collectionImage)
            item['collectionImage'] = collectionImage
            collectionName = li.xpath('./a/p//text()').extract_first()
            # print(collectionName)
            item['collectionName'] = collectionName
            url = 'http://www.dlnm.org.cn/' + li.xpath('./a/@href').extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc, meta={'item': item})
        if self.page_num <= 4:
            new_url = self.next_url % self.page_num
            self.page_num += 1
            yield scrapy.Request(new_url, callback=self.parse)

    def parse_desc(self, response):
        collectionIntroduction = response.xpath('//div[@class="abtxtbox"]/p/text()').extract()
        collectionIntroduction = ''.join(collectionIntroduction).strip()
        # print(collectionIntroduction)
        item = response.meta['item']
        item['collectionIntroduction'] = collectionIntroduction
