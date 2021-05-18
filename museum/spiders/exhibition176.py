# -*- coding: utf-8 -*-
import scrapy
from museum.items import exhibitionItem


class Exhibition176Spider(scrapy.Spider):
    name = 'exhibition176'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.918museum.org.cn/index.php/article/listarticle/pid/195/rel/thumb/sidebar/sidebar']

    def parse(self, response):
        li_list = response.xpath('//div[@class="article row "]/div')
        for li in li_list:
            item = exhibitionItem()
            exhibName = li.xpath('./a/div/text()').extract_first().strip()
            # print(exhibName)
            item['exhibName'] = exhibName
            url = 'http://www.918museum.org.cn' + li.xpath('./a/@href').extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc, meta={'item': item})

    def parse_desc(self, response):
        item = response.meta['item']
        exhibIntro = response.xpath('//div[@class="article_content"]/p//text()').extract()
        exhibIntro = ''.join(exhibIntro).strip()
        item['exhibIntro'] = exhibIntro
        # print(exhibIntro)
        exhibImg = response.xpath('//div[@class="article_content"]//img/@src').extract_first()
        if exhibImg != None and exhibImg[0] != 'h':
            exhibImg = 'http://www.918museum.org.cn' + exhibImg
        # print(exhibImg)
        item['exhibImg'] = exhibImg
