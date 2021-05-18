# -*- coding: utf-8 -*-
import scrapy


class Education183Spider(scrapy.Spider):
    name = 'education183'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.coalmus.org.cn/html/list_1650.html']

    def parse(self, response):
        li_list = response.xpath('//div[@id="LB"]/ul/li')
        for li in li_list:
            eduName = li.xpath('./h2/a/text()').extract_first().strip()
            # print(eduName)
            url = li.xpath('./h2/a/@href').extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc)

    def parse_desc(self, response):
        eduImg = str(response.xpath('//div[@id="MyContent"]/p/img/@src').extract_first())
        # print(eduImg)
        eduContent = response.xpath('//div[@id="MyContent"]/p//text()').extract()
        eduContent = ''.join(eduContent).strip()
        # print(eduContent)
