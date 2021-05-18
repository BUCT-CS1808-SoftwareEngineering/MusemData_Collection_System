# -*- coding: utf-8 -*-
import scrapy
from museum.items import collectionItem


class Collection178Spider(scrapy.Spider):
    name = 'collection178'
    # allowed_domains = ['www.xxx.com']
    # start_ruls = ['http://ordosbwg.org.cn/wwdz_121925/sq/']

    start_urls = ['http://ordosbwg.org.cn/wwdz_121925/sq/',
                  'http://ordosbwg.org.cn/wwdz_121925/tq/']

    def parse(self, response):
        li_list = response.xpath('//div[@class="collection-list-msg"]/ul/li')
        for li in li_list:
            item = collectionItem()
            collectionImage = response.url[:-1] + li.xpath('./a/img/@src').extract_first()[1:]
            # print(collectionImage)
            item['collectionImage'] = collectionImage
            collectionName = li.xpath('./a/p/a/text()').extract_first()
            # print(collectionName)
            item['collectionName'] = collectionName
            url = response.url + li.xpath('./a/p/a/@href').extract_first()[1:]
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc, meta={'item': item})

    def parse_desc(self, response):
        collectionIntroduction = response.xpath('//div[@class="details-p"]//text()').extract()
        collectionIntroduction = ''.join(collectionIntroduction).strip()
        # print(collectionIntroduction)
        item = response.meta['item']
        item['collectionIntroduction'] = collectionIntroduction
