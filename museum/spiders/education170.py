# -*- coding: utf-8 -*-
import scrapy


class Education170Spider(scrapy.Spider):
    name = 'education170'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://museum.nenu.edu.cn/kpjy/kphd.htm']

    def parse(self, response):
        li_list = response.xpath('//div[@class="con"]/ul/li')
        for li in li_list:
            eduName = li.xpath('./a//text()').extract_first().strip()
            # print(eduName)
            url = list(li.xpath('./a/@href').extract_first())[2:]
            url = ''.join(url)
            url = 'http://museum.nenu.edu.cn/' + url
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc)

    def parse_desc(self, response):
        eduImg = response.xpath('//div[@class="v_news_content"]/p/img/@src').extract_first()
        if eduImg != None:
            eduImg = 'http://museum.nenu.edu.cn/' + eduImg
        # print(eduImg)
        eduContent = response.xpath('//div[@class="v_news_content"]//text()').extract()
        eduContent = ''.join(eduContent).strip()
        # print(eduContent)
