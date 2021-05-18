# -*- coding: utf-8 -*-
import scrapy
from museum.items import collectionItem


class Collection174Spider(scrapy.Spider):
    name = 'collection174'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.dlmodernmuseum.com/collection/']
    next_url = 'https://www.dlmodernmuseum.com/collection/%d.html'
    page_num = 2

    def parse(self, response):
        li_list = response.xpath('//div[@class="showlist contrightlist"]/ul/li')
        for li in li_list:
            item = collectionItem()
            collectionImage = 'https://www.dlmodernmuseum.com' + li.xpath(
                './a/div[@class="showimg2"]/img/@src').extract_first()
            # print(collectionImage)
            item['collectionImage'] = collectionImage
            collectionName = li.xpath('./a/div[@class="showtitle2"]/text()').extract_first()
            # print(collectionName)
            item['collectionName'] = collectionName
            url = li.xpath('./a/@href').extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc, meta={'item': item})
        if self.page_num <= 7:
            new_url = self.next_url % self.page_num
            self.page_num += 1
            yield scrapy.Request(new_url, callback=self.parse)

    def parse_desc(self, response):
        collectionIntroduction = response.xpath('//div[@class="showlist contrightlist"]/p//text()').extract()
        collectionIntroduction = ''.join(collectionIntroduction).strip()
        # print(collectionIntroduction)
        item = response.meta['item']
        item['collectionIntroduction'] = collectionIntroduction
