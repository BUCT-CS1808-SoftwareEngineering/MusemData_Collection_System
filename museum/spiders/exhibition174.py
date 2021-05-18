# -*- coding: utf-8 -*-
import scrapy
from museum.items import exhibitionItem


class Exhibition174Spider(scrapy.Spider):
    name = 'exhibition174'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.dlmodernmuseum.com/exhibition/display/']

    def parse(self, response):
        li_list = response.xpath('//div[@class="showlist contrightlist"]/ul/li')
        for li in li_list:
            item = exhibitionItem()
            exhibName = li.xpath('./a/div[@class="showtitle1"]/text()').extract_first().strip()
            # print(exhibName)
            item['exhibName'] = exhibName
            url = li.xpath('./a/@href').extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc, meta={'item': item})

    def parse_desc(self, response):
        item = response.meta['item']
        exhibIntro = response.xpath('//div[@class="showlist contrightlist"]/p//text()').extract()
        exhibIntro = ''.join(exhibIntro).strip()
        item['exhibIntro'] = exhibIntro
        # print(exhibIntro)
        exhibImg = response.xpath('//div[@class="showlist contrightlist"]/p/img/@src').extract_first()
        if exhibImg != None and exhibImg[0] != 'h':
            exhibImg = 'https://www.dlmodernmuseum.com' + exhibImg
        # print(exhibImg)
        item['exhibImg'] = exhibImg
