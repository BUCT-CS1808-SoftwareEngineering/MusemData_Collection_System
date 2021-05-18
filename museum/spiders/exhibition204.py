# -*- coding: utf-8 -*-
import scrapy
from museum.items import exhibitionItem


class Exhibition204Spider(scrapy.Spider):
    name = 'exhibition204'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.wmhg.com.cn/permanent.html']

    def parse(self, response):
        li_list = response.xpath('//div[@class="list-item"]')
        for li in li_list:
            item = exhibitionItem()
            exhibName = li.xpath('.//div[@class="h18"]/a/text()').extract_first()
            # print(exhibName)
            item['exhibName'] = exhibName
            url = 'https://www.wmhg.com.cn' + li.xpath('.//div[@class="cont"]/div[@class="h18"]/a/@href').extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc, meta={'item': item})

    def parse_desc(self, response):
        item = response.meta['item']
        exhibIntro = response.xpath('//div[@class="text"]//text()').extract()
        exhibIntro = ''.join(exhibIntro).strip()
        item['exhibIntro'] = exhibIntro
        # print(exhibIntro)
        exhibImg = response.xpath('//div[@class="child"]/a/img/@src').extract_first()
        if exhibImg != None and exhibImg[0] != 'h':
            exhibImg = 'https://www.wmhg.com.cn' + exhibImg
        # print(exhibImg)
        item['exhibImg'] = exhibImg
