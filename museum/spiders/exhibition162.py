# -*- coding: utf-8 -*-
import scrapy
from museum.items import exhibitionItem


class Exhibition162Spider(scrapy.Spider):
    name = 'exhibition162'
    # allowed_domains = ['http://www.luxunmuseum.cn/news/index.html']
    start_urls = ['http://www.luxunmuseum.cn/news/index.html/']

    def parse(self, response):
        article_list = response.xpath('//div[@class="am-u-md-9 am-u-md-push-3"]/article')
        for article in article_list:
            item = exhibitionItem()
            exhibName = article.xpath('./h3/a/text()').extract_first()
            # print(exhibName)
            item['exhibName'] = exhibName
            url = 'http://www.luxunmuseum.cn' + article.xpath('./h3/a/@href').extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc, meta={'item': item})

    def parse_desc(self, response):
        item = response.meta['item']
        exhibIntro = response.xpath('//div[@class="am-cf "]/p/span//text()').extract()
        exhibIntro = ''.join(exhibIntro).strip()
        item['exhibIntro'] = exhibIntro
        # print(exhibIntro)
        exhibImg = response.xpath('//div[@class="am-cf "]//img/@src').extract_first()
        if exhibImg[0] != 'h':
            exhibImg = 'http://www.luxunmuseum.cn' + exhibImg
        # print(exhibImg)
        item['exhibImg'] = exhibImg
