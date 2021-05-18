# -*- coding: utf-8 -*-
import scrapy


class Education174Spider(scrapy.Spider):
    name = 'education174'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.dlmodernmuseum.com/activity/']

    def parse(self, response):
        li_list = response.xpath('//div[@class="infolist contrightlist"]/ul/li')
        for li in li_list:
            eduName = li.xpath('./a//text()').extract_first().strip()
            # print(eduName)
            url = li.xpath('./a/@href').extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc)

    def parse_desc(self, response):
        eduImg = response.xpath('//div[@class="showlist contrightlist"]//img/@src').extract_first()
        # print(eduImg)
        eduContent = response.xpath('//div[@class="showlist contrightlist"]/p//text()').extract()
        eduContent = ''.join(eduContent).strip()
        # print(eduContent)
