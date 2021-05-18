# -*- coding: utf-8 -*-
import scrapy


class Education171Spider(scrapy.Spider):
    name = 'education171'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.jlmuseum.org/learning/']

    def parse(self, response):
        li_list = response.xpath('//div[@class="list-txt"]/ul/li')
        for li in li_list:
            eduName = li.xpath('./a//text()').extract_first().strip()
            # print(eduName)
            url = 'http://www.jlmuseum.org' + li.xpath('./a/@href').extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc)

    def parse_desc(self, response):
        eduImg = str(response.xpath('//div[@class="cont"]//img/@src').extract_first())
        if eduImg != None and len(eduImg) > 50:
            eduImg = None
        # print(eduImg)
        eduContent = response.xpath('//div[@class="cont"]/p//text()').extract()
        eduContent = ''.join(eduContent).strip()
        # print(eduContent)
