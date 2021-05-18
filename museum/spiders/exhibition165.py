# -*- coding: utf-8 -*-
import scrapy
from museum.items import exhibitionItem


class Exhibition165Spider(scrapy.Spider):
    name = 'exhibition165'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.hljsmzbwg.com/zl.html']

    def parse(self, response):
        li_list = response.xpath('//ul[@class="pro_l clearfix"]/li')
        for li in li_list:
            item = exhibitionItem()
            exhibName = li.xpath('./a/p/text()').extract_first().strip()
            # print(exhibName)
            item['exhibName'] = exhibName
            url = 'http://www.hljsmzbwg.com/' + li.xpath('./a/@href').extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc, meta={'item': item})

    def parse_desc(self, response):
        item = response.meta['item']
        exhibIntro = response.xpath('//div[@class="scd_m"]//text()').extract()
        exhibIntro = ''.join(exhibIntro).strip()
        item['exhibIntro'] = exhibIntro
        # print(response.url)
        # print(exhibIntro)
        exhibImg = response.xpath('//div[@class="scd_m"]//img/@src').extract_first()
        # print(exhibImg)
        item['exhibImg'] = exhibImg
