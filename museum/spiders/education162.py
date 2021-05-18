# -*- coding: utf-8 -*-
import scrapy


class Education162Spider(scrapy.Spider):
    name = 'education162'
    # allowed_domains = ['http://www.luxunmuseum.cn/apage/index/cid/2.html']
    start_urls = ['http://www.luxunmuseum.cn/apage/index/cid/2.html/']

    def parse(self, response):
        article_list = response.xpath('//article[@class="blog-main"]')
        for article in article_list:
            eduName = article.xpath('./h3/a/text()').extract_first()
            # print(eduName)
            url = 'http://www.luxunmuseum.cn' + article.xpath('./h3/a/@href').extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc)

    def parse_desc(self, response):
        eduImg = response.xpath('//div[@class="am-g"]//img/@src').extract_first()
        # print(eduImg)
        eduContent = response.xpath('//div[@class="am-g"]//text()').extract()
        eduContent = ''.join(eduContent).strip()
        # print(eduContent) # 这里的内容有的只有一条链接
