# -*- coding: utf-8 -*-
import scrapy
from museum.items import collectionItem


class Collection180Spider(scrapy.Spider):
    name = 'collection180'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://neimenggubowuguan.meishujia.cn/?act=usite&said=354&usid=400',
                  'http://neimenggubowuguan.meishujia.cn/?page=2&act=usite&said=354&usid=400']

    def parse(self, response):
        li_list = response.xpath(
            '//dd[@class="theme_body_1231159117 theme_body_3705"]/ol/table[2]/tr/td/table')
        for li in li_list:
            item = collectionItem()
            collectionImage = 'http://neimenggubowuguan.meishujia.cn/' + li.xpath(
                './tr[1]/td/a/img/@src').extract_first()
            # print(collectionImage)
            item['collectionImage'] = collectionImage
            collectionName = li.xpath('./tr[2]/td/a/text()').extract_first()
            # print(collectionName)
            item['collectionName'] = collectionName
            url = 'http://neimenggubowuguan.meishujia.cn/' + li.xpath('./tr[2]/td/a/@href').extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc, meta={'item': item})

    def parse_desc(self, response):
        collectionIntroduction = response.xpath('//ul[@class="zl_r_b zl_r_bt"]//text()').extract()
        collectionIntroduction = ''.join(collectionIntroduction).strip()
        # print(collectionIntroduction)
        item = response.meta['item']
        item['collectionIntroduction'] = collectionIntroduction
