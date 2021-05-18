# -*- coding: utf-8 -*-
import scrapy
from museum.items import exhibitionItem


class Exhibition171Spider(scrapy.Spider):
    name = 'exhibition171'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.jlmuseum.org/display/']

    def parse(self, response):
        li_list = response.xpath('//ul[@class="pic-list"]/li')
        for li in li_list:
            item = exhibitionItem()
            exhibName = li.xpath('./div/div/a//text()').extract_first().strip()
            # print(exhibName)
            item['exhibName'] = exhibName
            url = 'http://www.jlmuseum.org' + li.xpath('./a/@href').extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc, meta={'item': item})

    def parse_desc(self, response):
        item = response.meta['item']
        exhibIntro = response.xpath('//div[@class="pics-cont"]/p/span//text()').extract()
        exhibIntro = ''.join(exhibIntro).strip()
        item['exhibIntro'] = exhibIntro
        # print(exhibIntro)
        exhibImg = response.xpath('//div[@class="pics-cont"]/p/img/@src').extract_first()
        if exhibImg != None and exhibImg[0] != 'h':
            exhibImg = 'http://www.jlmuseum.org' + exhibImg
        # print(exhibImg)
        item['exhibImg'] = exhibImg
