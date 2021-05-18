# -*- coding: utf-8 -*-
import scrapy
from museum.items import collectionItem


class Collection163Spider(scrapy.Spider):
    name = 'collection163'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.zgyd1921.com/zgyd/node3/n17/n18/index.html']
    next_url = 'http://www.zgyd1921.com/zgyd/node3/n17/n18/index%d.html'
    page_num = 1

    def parse(self, response):
        li_list = response.xpath('//ul[@class="piclist2"]/li')
        for li in li_list:
            item = collectionItem()
            collectionImage = 'http://www.zgyd1921.com' + li.xpath('./a/img/@src').extract_first()
            # print(collectionImage)
            item['collectionImage'] = collectionImage
            collectionName = li.xpath('./p/a//text()').extract_first()
            # print(collectionName)
            item['collectionName'] = collectionName
            url = 'http://www.zgyd1921.com' + li.xpath('./p/a/@href').extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc, meta={'item': item})
        if self.page_num <= 4:
            new_url = self.next_url % self.page_num
            self.page_num += 1
            yield scrapy.Request(new_url, callback=self.parse)

    def parse_desc(self, response):
        collectionIntroduction = response.xpath('//div[@class="grey14 lh30"]/p/text()').extract()
        collectionIntroduction = ''.join(collectionIntroduction).strip()
        # print(collectionIntroduction)
        item = response.meta['item']
        item['collectionIntroduction'] = collectionIntroduction
