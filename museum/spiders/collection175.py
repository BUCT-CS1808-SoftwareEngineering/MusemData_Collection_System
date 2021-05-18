# -*- coding: utf-8 -*-
import scrapy
from museum.items import collectionItem


class Collection175Spider(scrapy.Spider):
    name = 'collection175'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.lvshunmuseum.org/collection/product.aspx?SortID=9',
                  'http://www.lvshunmuseum.org/collection/product.aspx?SortID=9&Page=2',
                  'http://www.lvshunmuseum.org/collection/product.aspx?SortID=9&Page=3',
                  'http://www.lvshunmuseum.org/collection/product.aspx?SortID=9&Page=4',
                  'http://www.lvshunmuseum.org/collection/product.aspx?SortID=10',
                  'http://www.lvshunmuseum.org/collection/product.aspx?SortID=10&Page=2',
                  'http://www.lvshunmuseum.org/collection/product.aspx?SortID=10&Page=3',
                  'http://www.lvshunmuseum.org/collection/product.aspx?SortID=10&Page=4',
                  'http://www.lvshunmuseum.org/collection/product.aspx?SortID=11',
                  'http://www.lvshunmuseum.org/collection/product.aspx?SortID=11&Page=2',
                  'http://www.lvshunmuseum.org/collection/product.aspx?SortID=11&Page=3',
                  'http://www.lvshunmuseum.org/collection/product.aspx?SortID=11&Page=4',
                  'http://www.lvshunmuseum.org/collection/product.aspx?SortID=11&Page=5',
                  'http://www.lvshunmuseum.org/collection/product.aspx?SortID=12',
                  'http://www.lvshunmuseum.org/collection/product.aspx?SortID=12&Page=2',
                  'http://www.lvshunmuseum.org/collection/product.aspx?SortID=12&Page=3',
                  'http://www.lvshunmuseum.org/collection/product.aspx?SortID=12&Page=4',
                  'http://www.lvshunmuseum.org/collection/product.aspx?SortID=12&Page=5',
                  'http://www.lvshunmuseum.org/collection/product.aspx?SortID=13',
                  'http://www.lvshunmuseum.org/collection/product.aspx?SortID=13&Page=2',
                  'http://www.lvshunmuseum.org/collection/product.aspx?SortID=13&Page=3',
                  'http://www.lvshunmuseum.org/collection/product.aspx?SortID=13&Page=4',
                  'http://www.lvshunmuseum.org/collection/product.aspx?SortID=14',
                  'http://www.lvshunmuseum.org/collection/product.aspx?SortID=14&Page=2',
                  'http://www.lvshunmuseum.org/collection/product.aspx?SortID=14&Page=3',
                  'http://www.lvshunmuseum.org/collection/product.aspx?SortID=14&Page=4',
                  'http://www.lvshunmuseum.org/collection/product.aspx?SortID=14&Page=5',
                  'http://www.lvshunmuseum.org/collection/product.aspx?SortID=15',
                  'http://www.lvshunmuseum.org/collection/product.aspx?SortID=15&Page=2',
                  'http://www.lvshunmuseum.org/collection/product.aspx?SortID=15&Page=3',
                  'http://www.lvshunmuseum.org/collection/product.aspx?SortID=15&Page=4',
                  'http://www.lvshunmuseum.org/collection/product.aspx?SortID=16',
                  'http://www.lvshunmuseum.org/collection/product.aspx?SortID=16&Page=2',
                  'http://www.lvshunmuseum.org/collection/product.aspx?SortID=16&Page=3',
                  'http://www.lvshunmuseum.org/collection/product.aspx?SortID=17',
                  'http://www.lvshunmuseum.org/collection/product.aspx?SortID=17&Page=2',
                  'http://www.lvshunmuseum.org/collection/product.aspx?SortID=17&Page=3',
                  'http://www.lvshunmuseum.org/collection/product.aspx?SortID=17&Page=4']

    def parse(self, response):
        li_list = response.xpath('//ul[@class="showcase_list"]/li')
        for li in li_list:
            item = collectionItem()
            collectionImage = 'http://www.lvshunmuseum.org' + li.xpath('./a/div[@class="picbox"]/img/@src').extract_first().strip()
            # print(collectionImage)
            item['collectionImage'] = collectionImage
            collectionName = li.xpath('./a/div[@class="textbox textbox2"]/h1/text()').extract_first()
            # print(collectionName)
            item['collectionName'] = collectionName
            url = 'http://www.lvshunmuseum.org' + li.xpath('./a/@href').extract_first().strip()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc, meta={'item': item})

    def parse_desc(self, response):
        collectionIntroduction = response.xpath('//p[@class="MsoNormal"]//text()').extract()
        collectionIntroduction = ''.join(collectionIntroduction).strip()
        # print(collectionIntroduction)
        item = response.meta['item']
        item['collectionIntroduction'] = collectionIntroduction
