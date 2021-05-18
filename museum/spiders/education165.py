# -*- coding: utf-8 -*-
import scrapy


class Education165Spider(scrapy.Spider):
    name = 'education165'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.hljsmzbwg.com/jyhd.html']

    def parse(self, response):
        li_list = response.xpath('//div[@class="news"]/dl')
        for li in li_list:
            eduName = li.xpath('./dd/div[@class="title"]/a/text()').extract_first().strip()
            # print(eduName)
            url = 'http://www.hljsmzbwg.com/' + li.xpath('./dt/a/@href').extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc)

    def parse_desc(self, response):
        eduImg = response.xpath('//div[@class="scd_m"]//img/@src').extract_first()
        # print(eduImg)
        eduContent = response.xpath('//div[@class="scd_m"]/p/span//text()').extract()
        eduContent = ''.join(eduContent).strip()
        # print(eduContent)
