# -*- coding: utf-8 -*-
import scrapy
from museum.items import collectionItem


class Collection161Spider(scrapy.Spider):
    name = 'collection161'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.cyjng.net/Default.aspx?tabid=62&language=zh-CN']

    def parse(self, response):
        label_a = response.xpath('//a[@class="Normal"]')
        collectionName = label_a.xpath('.//text()').extract()
        url_list = label_a.xpath('./@href').extract()
        for i in range(len(url_list)):
            item = collectionItem()
            item['collectionName'] = collectionName[i]
            # print(collectionName[i])
            url = 'http://www.cyjng.net' + url_list[i]
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc, meta={'item': item}, dont_filter=True)

    def parse_desc(self, response):
        item = response.meta['item']
        collectionIntroduction = response.xpath(
            '//span[@id="dnn_ctr504_ArticleDetails_ctl00_lblArticle"]//text()').extract_first()
        # print(collectionIntroduction)
        collectionImage = 'http://www.cyjng.net' + response.xpath(
            '//img[@id="dnn_ctr504_ArticleDetails_ctl00_imgArticleImage"]/@src').extract_first()
        # print(collectionImage)
        item['collectionIntroduction'] = collectionIntroduction
        item['collectionImage'] = collectionImage
        # yield item
