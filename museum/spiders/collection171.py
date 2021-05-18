# -*- coding: utf-8 -*-
import scrapy
from museum.items import collectionItem


class Collection171Spider(scrapy.Spider):
    name = 'collection171'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.jlmuseum.org/collection/']
    next_url = 'http://www.jlmuseum.org/collection/%d.html'
    page_num = 2

    def parse(self, response):
        li_list = response.xpath('//div[@class="list-pics"]/ul/li')
        for li in li_list:
            item = collectionItem()
            collectionImage = 'http://www.jlmuseum.org' + li.xpath('./div/a/img/@src').extract_first()
            # print(collectionImage)
            item['collectionImage'] = collectionImage
            collectionName = li.xpath('./div[@class="info"]/a//text()').extract_first()
            # print(collectionName)
            item['collectionName'] = collectionName
            url = 'http://www.jlmuseum.org' + li.xpath('./div/a/@href').extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc, meta={'item': item})
        if self.page_num <= 3:
            new_url = self.next_url % self.page_num
            self.page_num += 1
            yield scrapy.Request(new_url, callback=self.parse)

    def parse_desc(self, response):
        collectionIntroduction = response.xpath('//div[@class="pics-cont"]//text()').extract()
        collectionIntroduction = ''.join(collectionIntroduction).strip()
        # print(collectionIntroduction)
        item = response.meta['item']
        item['collectionIntroduction'] = collectionIntroduction
