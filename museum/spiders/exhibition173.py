# -*- coding: utf-8 -*-
import scrapy
from museum.items import exhibitionItem


class Exhibition173Spider(scrapy.Spider):
    name = 'exhibition173'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.sypm.org.cn/products_list/&pmcId=56&comp_stats=comp-FrontProductsCategory_show01-1277800417102.html']

    def parse(self, response):
        li_list = response.xpath('//ul[@class="mainul productlist-02"]/li[@class="content column-num4"]')
        for li in li_list:
            item = exhibitionItem()
            exhibName = li.xpath('.//div[@class="pro-module"]/ul/li/h1/strong/a/text()').extract_first().strip()
            # print(exhibName)
            item['exhibName'] = exhibName
            url = 'http://www.sypm.org.cn/' + li.xpath('.//div[@class="pro-module"]/ul/li/h1/strong/a/@href').extract_first()
            # print(url)
            exhibImg = li.xpath('.//div[@class="pic-module"]/div/a/img/@src').extract_first()
            if exhibImg[0] != 'h':
                exhibImg = 'http://www.sypm.org.cn/' + exhibImg
            # print(exhibImg)
            item['exhibImg'] = exhibImg
            yield scrapy.Request(url, callback=self.parse_desc, meta={'item': item})

    def parse_desc(self, response):
        item = response.meta['item']
        exhibIntro = response.xpath('//li[@class="name1"]/text()').extract()
        exhibIntro = ''.join(exhibIntro).strip()
        item['exhibIntro'] = exhibIntro
        # print(exhibIntro)
