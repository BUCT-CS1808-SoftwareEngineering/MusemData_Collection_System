# -*- coding: utf-8 -*-
import scrapy


class Education163Spider(scrapy.Spider):
    name = 'education163'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.zgyd1921.com/zgyd/node3/n23/n24/index.html']

    def parse(self, response):
        li_list = response.xpath('//ul[@class="list1"]/li')
        for li in li_list:
            eduName = li.xpath('./a//text()').extract_first().strip()
            # print(eduName)
            url = 'http://www.zgyd1921.com' + li.xpath('./a/@href').extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc)

    def parse_desc(self, response):
        eduImg = str(response.xpath('//div[@class="grey14 lh30"]/div/img/@src').extract_first())
        if len(eduImg) > 50:
            eduImg = None
        # print(eduImg)
        eduContent = response.xpath('//div[@class="grey14 lh30"]/p//text()').extract()
        eduContent = ''.join(eduContent).strip()
        # print(eduContent)
