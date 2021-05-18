# -*- coding: utf-8 -*-
import scrapy
from museum.items import collectionItem


class Collection173Spider(scrapy.Spider):
    name = 'collection173'
    # allowed_domains = ['www.xxx.com']
    start_urls = [
        'http://www.sypm.org.cn/products_list3/&pmcId=77&comp_stats=comp-FrontProductsCategory_show01-ycjd.html']
    next_url = 'http://www.sypm.org.cn/products_list3/&pmcId=77&comp_stats=comp-FrontProductsCategory_show01-ycjd&pageNo_FrontProducts_list01-0042=%d&pageSize_FrontProducts_list01-0042=20.html#'
    page_num = 2

    def parse(self, response):
        li_list = response.xpath('//ul[@class="mainul productlist-02"]/li[@class="content column-num4"]')
        for li in li_list:
            item = collectionItem()
            collectionImage = li.xpath('./div/div/a/img/@src').extract_first()
            if collectionImage != None:
                collectionImage = 'http://www.sypm.org.cn/' + collectionImage
            # print(collectionImage)
            item['collectionImage'] = collectionImage
            collectionName = li.xpath('./div[@class="pro-module"]/ul/li/h1/strong/a/text()').extract_first().strip()
            # print(collectionName)
            item['collectionName'] = collectionName
            url = 'http://www.sypm.org.cn/' + li.xpath('./div[@class="pic-module"]/div[@class="pic"]/a/@href').extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc, meta={'item': item})
        if self.page_num <= 40:
            new_url = self.next_url % self.page_num
            self.page_num += 1
            yield scrapy.Request(new_url, callback=self.parse)

    def parse_desc(self, response):
        collectionIntroduction = response.xpath('//div[@class="detail"]/div/div/text()').extract()
        collectionIntroduction = ''.join(collectionIntroduction).strip()
        # print(collectionIntroduction)
        item = response.meta['item']
        item['collectionIntroduction'] = collectionIntroduction
