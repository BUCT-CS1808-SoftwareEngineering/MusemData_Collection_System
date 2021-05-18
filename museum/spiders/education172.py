# -*- coding: utf-8 -*-
import scrapy


class Education172Spider(scrapy.Spider):
    name = 'education172'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.dlnm.org.cn/?_f=education&type=5']

    def parse(self, response):
        li_list = response.xpath('//ul[@class="newsnoticelist"]/li')
        for li in li_list:
            eduName = li.xpath('./a/div/h4/text()').extract_first().strip()
            # print(eduName)
            url = li.xpath('./a/@href').extract_first()
            if url != None and url[0] != 'h':
                url = 'http://www.dlnm.org.cn/' + url
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc)

    def parse_desc(self, response):
        eduImg = str(response.xpath('//div[@class="rich_media_content "]/section//img/@data-src').extract_first())
        # print(eduImg)
        eduContent = response.xpath('//div[@class="rich_media_content "]/section//text()').extract()
        eduContent = ''.join(eduContent).strip()
        # print(eduContent)
