# -*- coding: utf-8 -*-
import scrapy
from museum.items import collectionItem


class Collection165Spider(scrapy.Spider):
    name = 'collection165'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.hljsmzbwg.com/cp.html']
    next_url = 'http://www.hljsmzbwg.com/cp_%d.html'
    page_num = 2

    def parse(self, response):
        li_list = response.xpath('//ul[@class="pro_l clearfix"]/li')
        for li in li_list:
            item = collectionItem()
            collectionImage = li.xpath('./a/img/@src').extract_first()
            print(collectionImage)
            item['collectionImage'] = collectionImage
            collectionName = li.xpath('./a/p/text()').extract_first()
            # print(collectionName)
            item['collectionName'] = collectionName
            url = 'http://www.hljsmzbwg.com/' + li.xpath('./a/@href').extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc, meta={'item': item})
        # if self.page_num <= 340:
        #     new_url = self.next_url % self.page_num
        #     self.page_num += 1
        #     yield scrapy.Request(new_url, callback=self.parse)

    def parse_desc(self, response):
        collectionIntroduction = response.xpath('//section[@class="96wxDiy"]/p/span//text()').extract()
        collectionIntroduction = ''.join(collectionIntroduction)
        # print(collectionIntroduction)
        item = response.meta['item']
        item['collectionIntroduction'] = collectionIntroduction
