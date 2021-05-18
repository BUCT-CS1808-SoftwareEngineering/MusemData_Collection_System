# -*- coding: utf-8 -*-
import scrapy


class Education204Spider(scrapy.Spider):
    name = 'education204'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.wmhg.com.cn/activity/detail/1945.html',
                  'https://www.wmhg.com.cn/activity/detail/1943.html',
                  'https://www.wmhg.com.cn/activity/detail/1940.html',
                  'https://www.wmhg.com.cn/activity/detail/1918.html']

    def parse(self, response):
        eduName = response.xpath('//div[@class="x-wrap"]/div/text()').extract_first().strip()
        # print(eduName)
        eduImg = 'https://www.wmhg.com.cn' + response.xpath('//div[@class="p"]//img/@src').extract_first()
        # print(eduImg)
        eduContent = response.xpath('//div[@class="p"]/p/span//text()').extract()
        eduContent = ''.join(eduContent).strip()
        # print(eduContent)
