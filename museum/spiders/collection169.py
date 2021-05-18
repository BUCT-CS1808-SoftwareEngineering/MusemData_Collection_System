# -*- coding: utf-8 -*-
import scrapy
from museum.items import collectionItem


class Collection169Spider(scrapy.Spider):
    name = 'collection169'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.hljmuseum.com/cpgz/cpxs/zgzb/', 'http://www.hljmuseum.com/cpgz/cpxs/lsww/',
                  'http://www.hljmuseum.com/system/more/cpgz/cpxs/lsww/index/page_01.html',
                  'http://www.hljmuseum.com/system/more/cpgz/cpxs/lsww/index/page_02.html',
                  'http://www.hljmuseum.com/system/more/cpgz/cpxs/lsww/index/page_03.html',
                  'http://www.hljmuseum.com/system/more/cpgz/cpxs/lsww/index/page_04.html',
                  'http://www.hljmuseum.com/system/more/cpgz/cpxs/lsww/index/page_05.html',
                  'http://www.hljmuseum.com/system/more/cpgz/cpxs/lsww/index/page_06.html',
                  'http://www.hljmuseum.com/system/more/cpgz/cpxs/lsww/index/page_07.html',
                  'http://www.hljmuseum.com/cpgz/cpxs/zrbb/', 'http://www.hljmuseum.com/cpgz/cpxs/yscp/',
                  'http://www.hljmuseum.com/cpgz/cpxs/wxzl/']

    def parse(self, response):
        li_list = response.xpath('//ul[@class="titlepic05 huis"]/div/li')
        for li in li_list:
            item = collectionItem()
            collectionImage = li.xpath('./a/img/@src').extract_first()
            # print(collectionImage)
            item['collectionImage'] = collectionImage
            collectionName = li.xpath('./a/span//text()').extract_first()
            # print(collectionName)
            item['collectionName'] = collectionName
            url = 'http://www.hljmuseum.com' + li.xpath('./a/@href').extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc, meta={'item': item})

    def parse_desc(self, response):
        collectionIntroduction = response.xpath('//div[@class="duanluo"]/p/span//text()').extract()
        collectionIntroduction = ''.join(collectionIntroduction)
        # print(collectionIntroduction)
        item = response.meta['item']
        item['collectionIntroduction'] = collectionIntroduction
