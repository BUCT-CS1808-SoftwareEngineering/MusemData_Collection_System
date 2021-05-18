# -*- coding: utf-8 -*-
import scrapy
from museum.items import collectionItem


class Collection204Spider(scrapy.Spider):
    name = 'collection204'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.wmhg.com.cn/searchs/collection.html?tpl_file=collection_list&pagesize=100',
                  'https://www.wmhg.com.cn/searchs/collection/tpl_file/collection_list/pagesize/9/site_id/0/p/2.html',
                  'https://www.wmhg.com.cn/searchs/collection/tpl_file/collection_list/pagesize/9/site_id/0/p/3.html',
                  'https://www.wmhg.com.cn/searchs/collection/tpl_file/collection_list/pagesize/9/site_id/0/p/4.html']

    def parse(self, response):
        li_list = response.xpath('//div[@class="list-item"]')
        for li in li_list:
            item = collectionItem()
            collectionName = li.xpath('./a/span[2]/text()').extract_first()
            item['collectionName'] = collectionName
            # print(collectionName)
            url = 'https://www.wmhg.com.cn' + li.xpath('./a/@href').extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc, meta={'item': item})

    def parse_desc(self, response):
        item = response.meta['item']
        collectionIntroduction = response.xpath('//div[@class="p"]/p[2]/span//text()').extract_first()
        item['collectionIntroduction'] = collectionIntroduction
        # print(collectionIntroduction)
        collectionImage = 'https://www.wmhg.com.cn' + response.xpath('//div[@class="img"]/img/@src').extract_first()
        item['collectionImage'] = collectionImage
        # print(collectionImage)
