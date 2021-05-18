# -*- coding: utf-8 -*-
import scrapy
from museum.items import exhibitionItem


class Exhibition172Spider(scrapy.Spider):
    name = 'exhibition172'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.dlnm.org.cn/?_f=showroom']

    def parse(self, response):
        li_list = response.xpath('//ul[@class="themelist"]/li')
        for li in li_list:
            item = exhibitionItem()
            exhibName = li.xpath('./a/p/text()').extract_first().strip()
            # print(exhibName)
            item['exhibName'] = exhibName
            url = 'http://www.dlnm.org.cn/' + li.xpath('./a/@href').extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc, meta={'item': item})

    def parse_desc(self, response):
        item = response.meta['item']
        exhibIntro = response.xpath('//div[@class="abtxtbox"]/p//text()').extract()
        exhibIntro = ''.join(exhibIntro).strip()
        item['exhibIntro'] = exhibIntro
        # print(exhibIntro)
        exhibImg = response.xpath('//div[@class="abtxtbox"]/p/img/@src').extract_first()
        if exhibImg[0] != 'h':
            exhibImg = 'http://www.zgyd1921.com' + exhibImg
        # print(exhibImg)
        item['exhibImg'] = exhibImg
