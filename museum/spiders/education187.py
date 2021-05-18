# -*- coding: utf-8 -*-
import scrapy


class Education187Spider(scrapy.Spider):
    name = 'education187'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.hebeimuseum.org.cn/channels/30.html']

    def parse(self, response):
        li_list = response.xpath('//div[@class="list"]/ul/li')
        for li in li_list:
            eduName = li.xpath('./h4/a/text()').extract_first().strip()
            # print(eduName)
            url = 'http://www.hebeimuseum.org.cn' + li.xpath('./h4/a/@href').extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc)

    def parse_desc(self, response):
        eduImg = response.xpath('//div[@class="bd"]//img/@src').extract_first()
        if eduImg != None:
            eduImg = 'http://www.hebeimuseum.org.cn' + eduImg
        # print(eduImg)
        eduContent = response.xpath('//div[@class="bd"]/p//text()').extract()
        eduContent = ''.join(eduContent).strip()
        # print(eduContent)
