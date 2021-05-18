# -*- coding: utf-8 -*-
import scrapy
from museum.items import educationItem


class Education161Spider(scrapy.Spider):
    name = 'education161'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.cyjng.net/Default.aspx?tabid=79&language=zh-CN']

    def parse(self, response):
        a_list = response.xpath('//a[@class="Normal"]')
        for a in a_list:
            item = educationItem()
            eduName = a.xpath('.//text()').extract_first()
            item['eduName'] = eduName
            url = a.xpath('./@href').extract_first()
            if url[0] != 'h':
                url = 'http://www.cyjng.net' + url
            yield scrapy.Request(url, callback=self.parse_desc, meta={'item': item})

    def parse_desc(self, response):
        item = response.meta['item']
        eduContent = response.xpath('//div[@class="Article"]/table[2]/tbody/tr/td/table/tbody/tr/td//text()').extract()
        eduContent = ''.join(eduContent).strip()
        eduImg = response.xpath('//div[@class="Article"]//img/@src').extract_first()
        if eduImg != None:
            eduImg = 'http://www.cyjng.net' + eduImg
        item['eduImg'] = eduImg
        item['eduContent'] = eduContent
        # yield item
