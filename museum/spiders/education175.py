# -*- coding: utf-8 -*-
import scrapy


class Education175Spider(scrapy.Spider):
    name = 'education175'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.lvshunmuseum.org/Academic/']

    def parse(self, response):
        li_list = response.xpath('//ul[@class="showcase_list"]/li')
        for li in li_list:
            url = 'http://www.lvshunmuseum.org' + li.xpath('./a/@href').extract_first().strip()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc)

    def parse_desc(self, response):
        eduName = response.xpath('//div[@class="newsdetail_title"]/h1/text()').extract_first()
        # print(eduName)
        eduImg = response.xpath('//div[@class="newsdetail_content"]//img/@src').extract_first()
        if eduImg != None:
            eduImg = 'http://www.lvshunmuseum.org' + eduImg
        # print(eduImg)
        eduContent = response.xpath('//div[@class="newsdetail_content"]/p//text()').extract()
        eduContent = ''.join(eduContent).strip()
        # print(eduContent)
