# -*- coding: utf-8 -*-
import scrapy


class Education173Spider(scrapy.Spider):
    name = 'education173'
    # allowed_domains = ['www.xxx.com']
    start_urls = [
        'http://www.sypm.org.cn/news_list2/&newsCategoryId=74&comp_stats=comp-FrontNewsCategory_tree01-shjy.html']

    def parse(self, response):
        li_list = response.xpath('//ul[@class="comstyle newslist-01"]/li[@class="content column-num1"]')
        for li in li_list:
            eduName = li.xpath('./div/ul/li/h3/a/text()').extract_first().strip()
            # print(eduName)
            url = 'http://www.sypm.org.cn' + li.xpath('./div/ul/li/h3/a/@href').extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc)

    def parse_desc(self, response):
        eduImg = str(response.xpath('//div[@class="describe htmledit"]//img/@src').extract_first())
        if len(eduImg) > 50:
            eduImg = None
        # print(eduImg)
        eduContent = response.xpath('//div[@class="describe htmledit"]/p/text()').extract()
        eduContent = ''.join(eduContent).strip()
        # print(eduContent)
