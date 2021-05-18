# -*- coding: utf-8 -*-
import scrapy
from museum.items import exhibitionItem


class Exhibition186Spider(scrapy.Spider):
    name = 'exhibition186'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xbpjng.cn//News/NewsList_New.aspx?id=795']

    def parse(self, response):
        li_list = response.xpath('//div[@class="all-content"]/h2')
        for li in li_list:
            item = exhibitionItem()
            exhibName = li.xpath('./a//text()').extract_first().strip()
            # print(exhibName)
            item['exhibName'] = exhibName
            url = 'http://www.xbpjng.cn//News/' + li.xpath('./a/@href').extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc, meta={'item': item})

    def parse_desc(self, response):
        item = response.meta['item']
        exhibIntro = response.xpath('//span[@id="lb_Content"]/p/span//text()').extract()
        exhibIntro = ''.join(exhibIntro).strip()
        item['exhibIntro'] = exhibIntro
        # print(exhibIntro)
        exhibImg = str(response.xpath('//span[@id="lb_Content"]/p/img/@src').extract_first())
        if len(exhibImg) > 50:
            exhibImg = None
        # print(exhibImg)
        item['exhibImg'] = exhibImg
