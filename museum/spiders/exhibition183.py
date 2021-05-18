# -*- coding: utf-8 -*-
import scrapy
from museum.items import exhibitionItem


class Exhibition183Spider(scrapy.Spider):
    name = 'exhibition183'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.coalmus.org.cn/html/list_1659.html']

    def parse(self, response):
        li_list = response.xpath('//div[@id="LB"]/ul/li')
        for li in li_list:
            item = exhibitionItem()
            exhibName = li.xpath('./h2/a/text()').extract_first().strip()
            # print(exhibName)
            item['exhibName'] = exhibName
            url = li.xpath('./h2/a/@href').extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc, meta={'item': item})

    def parse_desc(self, response):
        item = response.meta['item']
        exhibIntro = response.xpath('//div[@id="MyContent"]/p//text()').extract()
        exhibIntro = ''.join(exhibIntro).strip()
        item['exhibIntro'] = exhibIntro
        # print(exhibIntro)
        exhibImg = response.xpath('//div[@id="MyContent"]/p/img/@src').extract_first()
        if exhibImg != None:
            exhibImg = 'http://www.coalmus.org.cn/' + exhibImg
        # print(exhibImg)
        item['exhibImg'] = exhibImg
