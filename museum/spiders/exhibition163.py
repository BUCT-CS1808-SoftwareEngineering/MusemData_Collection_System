# -*- coding: utf-8 -*-
import scrapy
from museum.items import exhibitionItem


class Exhibition163Spider(scrapy.Spider):
    name = 'exhibition163'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.zgyd1921.com/zgyd/node3/n11/n12/index.html']

    def parse(self, response):
        li_list = response.xpath('//ul[@class="piclist3"]/li')
        for li in li_list:
            item = exhibitionItem()
            exhibName = li.xpath('.//p[@class="name"]/a//text()').extract_first().strip()
            # print(exhibName)
            item['exhibName'] = exhibName
            url = 'http://www.zgyd1921.com' + li.xpath('./a/@href').extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc, meta={'item': item})

    def parse_desc(self, response):
        item = response.meta['item']
        exhibIntro = response.xpath('//div[@class="grey14 lh30"]/p//text()').extract()
        exhibIntro = ''.join(exhibIntro).strip()
        item['exhibIntro'] = exhibIntro
        # print(exhibIntro)
        exhibImg = response.xpath('//div[@class="grey14 lh30"]/div/img/@src').extract_first()
        if exhibImg[0] != 'h':
            exhibImg = 'http://www.zgyd1921.com' + exhibImg
        # print(exhibImg)  # 超级长
        item['exhibImg'] = exhibImg
