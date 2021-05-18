# -*- coding: utf-8 -*-
import scrapy
from museum.items import collectionItem


class Collection176Spider(scrapy.Spider):
    name = 'collection176'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.918museum.org.cn/index.php/article/listarticle/pid/126/rel/thumb/sidebar/sidebar']
    next_url = 'http://www.918museum.org.cn/index.php/article/listarticle/pid/126/rel/thumb/sidebar/sidebar?currentPage=%d'
    page_num = 2

    def parse(self, response):
        li_list = response.xpath('//div[@class="article row "]/div')
        for li in li_list:
            item = collectionItem()
            collectionImage = 'http://www.918museum.org.cn/' + li.xpath('./a/img/@src').extract_first()
            # print(collectionImage)
            item['collectionImage'] = collectionImage
            collectionName = li.xpath('./a/div[@class="caption"]/text()').extract_first().strip()
            # print(collectionName)
            item['collectionName'] = collectionName
            url = 'http://www.918museum.org.cn/' + li.xpath('./a/@href').extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc, meta={'item': item})
        if self.page_num <= 16:
            new_url = self.next_url % self.page_num
            self.page_num += 1
            yield scrapy.Request(new_url, callback=self.parse)

    def parse_desc(self, response):
        collectionIntroduction = response.xpath('//div[@class="article_content"]/p/text()').extract()
        collectionIntroduction = ''.join(collectionIntroduction).strip()
        # print(collectionIntroduction)
        item = response.meta['item']
        item['collectionIntroduction'] = collectionIntroduction
