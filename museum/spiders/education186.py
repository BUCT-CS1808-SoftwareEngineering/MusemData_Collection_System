# -*- coding: utf-8 -*-
import scrapy


class Education186Spider(scrapy.Spider):
    name = 'education186'
    # allowed_domains = ['www.xxx.com']
    start_urls = [
        'http://www.xbpjng.cn/wenbotiandi/chenlie.aspx?c=2ab3fba2-98d3-4d7c-9eb0-8cfe6d982a71&z=c700e111-ca4b-4689-91c6-84f5f84a9557']

    def parse(self, response):
        li_list = response.xpath('//div[@class="all-content"]/h2')
        for li in li_list:
            eduName = li.xpath('./a/text()').extract_first().strip()
            # print(eduName)
            url = 'http://www.xbpjng.cn/wenbotiandi/' + li.xpath('./a/@href').extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc)

    def parse_desc(self, response):
        eduImg = response.xpath('//div[@class="newcont"]/p//img/@src').extract_first()
        if eduImg != None and len(eduImg) > 100:
            eduImg = None
        # print(eduImg)
        eduContent = response.xpath('//div[@class="newcont"]/p//text()').extract()
        eduContent = ''.join(eduContent).strip()
        # print(eduContent)
