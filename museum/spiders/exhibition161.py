# -*- coding: utf-8 -*-
import scrapy
from museum.items import exhibitionItem


class Exhibition161Spider(scrapy.Spider):
    name = 'exhibition161'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.cyjng.net/Default.aspx?tabid=105&language=zh-CN']

    def parse(self, response):
        url_list = response.xpath('//span[@id="dnn_dnnLINKS_lblLinks"]/div/a/@href').extract()
        name_list = response.xpath('//span[@id="dnn_dnnLINKS_lblLinks"]/div/a/text()').extract()
        for i in range(1, len(url_list)):
            item = exhibitionItem()
            url = 'http://www.cyjng.net' + url_list[i]
            item['exhibName'] = name_list[i]
            # print(name_list[i], url)
            yield scrapy.Request(url, callback=self.parse_desc, meta={'item': item})

    def parse_desc(self, response):
        item = response.meta['item']
        exhibIntro = response.xpath(
            '//div[@class="Normal"]/text() | //div[@class="Normal"]/div//text() | //div[@class="Normal"]/table//text()').extract()
        exhibIntro = ''.join(exhibIntro).strip()
        exhibImg = 'http://www.cyjng.net' + response.xpath('//div[@class="Normal"]//img/@src').extract_first()
        # print(response.url, exhibIntro)
        item['exhibIntro'] = exhibIntro
        item['exhibImg'] = exhibImg
