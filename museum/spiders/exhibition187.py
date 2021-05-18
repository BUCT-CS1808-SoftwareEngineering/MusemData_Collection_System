# -*- coding: utf-8 -*-
import scrapy
from museum.items import exhibitionItem


class Exhibition187Spider(scrapy.Spider):
    name = 'exhibition187'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.hebeimuseum.org.cn/channels/12.html']

    def parse(self, response):
        li_list = response.xpath('//div[@class="list"]/ul/li')
        for li in li_list:
            item = exhibitionItem()
            exhibName = li.xpath('./dl/dd/a/text()').extract_first().strip()
            # print(exhibName)
            item['exhibName'] = exhibName
            url = 'http://www.hebeimuseum.org.cn' + li.xpath('./dl/dd/a/@href').extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc, meta={'item': item})

    def parse_desc(self, response):
        item = response.meta['item']
        exhibIntro = response.xpath('//div[@class="text"]/p//text()').extract()
        exhibIntro = ''.join(exhibIntro).strip()
        item['exhibIntro'] = exhibIntro
        # print(exhibIntro)
        exhibImg = response.xpath('//div[@id="focus"]//img/@src').extract_first()
        if exhibImg != None:
            exhibImg = 'http://www.hebeimuseum.org.cn' + exhibImg
        # print(exhibImg)
        item['exhibImg'] = exhibImg
