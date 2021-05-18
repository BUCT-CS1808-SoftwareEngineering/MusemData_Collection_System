# -*- coding: utf-8 -*-
import scrapy
from museum.items import collectionItem


class Exhibition170Spider(scrapy.Spider):
    name = 'exhibition170'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://museum.nenu.edu.cn/zlcl/jbcl.htm']

    def parse(self, response):
        li_list = response.xpath('//div[@class="con"]/ul/li')
        for li in li_list:
            item = collectionItem()
            collectionName = li.xpath('./a//text()').extract_first()
            # print(collectionName)
            item['collectionName'] = collectionName
            url = list(li.xpath('./a/@href').extract_first())[2:]
            url = ''.join(url)
            url = 'http://museum.nenu.edu.cn/' + url
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc, meta={'item': item})

    def parse_desc(self, response):
        collectionIntroduction = response.xpath('//div[@class="v_news_content"]/p//text()').extract()
        collectionIntroduction = ''.join(collectionIntroduction).strip()
        # print(collectionIntroduction)
        item = response.meta['item']
        item['collectionIntroduction'] = collectionIntroduction
        collectionImage = response.xpath('//div[@class="v_news_content"]//img/@src').extract_first()
        if collectionImage != None:
            collectionImage = 'http://museum.nenu.edu.cn' + collectionImage
        # print(collectionImage)
        item['collectionImage'] = collectionImage
