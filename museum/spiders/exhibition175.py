# -*- coding: utf-8 -*-
import scrapy
from museum.items import exhibitionItem


class Exhibition175Spider(scrapy.Spider):
    name = 'exhibition175'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.lvshunmuseum.org/Exhibition/']

    def parse(self, response):
        li_list = response.xpath('//ul[@class="showcase_list"]/li')
        for li in li_list:
            item = exhibitionItem()
            exhibName = li.xpath('./a/div[@class="textbox"]/h1/text()').extract_first().strip()
            # print(exhibName)
            item['exhibName'] = exhibName
            url = 'http://www.lvshunmuseum.org' + li.xpath('./a/@href').extract_first().strip()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc, meta={'item': item})

    def parse_desc(self, response):
        item = response.meta['item']
        exhibIntro = response.xpath('//div[@class="textshow"]/text()').extract()
        exhibIntro = ''.join(exhibIntro).strip()
        item['exhibIntro'] = exhibIntro
        # print(exhibIntro)
        exhibImg = 'http://www.lvshunmuseum.org'+response.xpath('//div[@class="showcase_detail"]//img/@src').extract_first().strip()
        # print(exhibImg)
        item['exhibImg'] = exhibImg
