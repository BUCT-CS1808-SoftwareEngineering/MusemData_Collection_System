# -*- coding: utf-8 -*-
import scrapy


class Education176Spider(scrapy.Spider):
    name = 'education176'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.918museum.org.cn/index.php/article/listarticle/pid/152/rel/detail/sidebar/sidebar']

    def parse(self, response):
        eduName = response.xpath('//div[@class="article_title"]/text()').extract_first().strip()
        # print(eduName)
        eduImg = 'http://www.918museum.org.cn' + response.xpath(
            '//div[@class="article_content"]//img/@src').extract_first()
        # print(eduImg)
        eduContent = response.xpath('//div[@class="article_content"]/p/text()').extract()
        eduContent = ''.join(eduContent).strip()
        # print(eduContent)
