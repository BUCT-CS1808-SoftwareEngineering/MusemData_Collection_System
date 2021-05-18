# -*- coding: utf-8 -*-
import scrapy
from museum.items import exhibitionItem


class Exhibition184Spider(scrapy.Spider):
    name = 'exhibition184'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.balujun.cn/e/action/ShowInfo.php?classid=8&id=2339',
                  'http://www.balujun.cn/e/action/ShowInfo.php?classid=8&id=2347',
                  'http://www.balujun.cn/e/action/ShowInfo.php?classid=8&id=2342',
                  'http://www.balujun.cn/e/action/ShowInfo.php?classid=8&id=2340']

    def parse(self, response):
        item = exhibitionItem()
        exhibName = response.xpath('.//div[@class="content-title"]/h3/text()').extract_first().strip()
        # print(exhibName)
        item['exhibName'] = exhibName
        exhibIntro = response.xpath('//div[@class="v_news_content"]/p//text()').extract()
        exhibIntro = ''.join(exhibIntro).strip()
        item['exhibIntro'] = exhibIntro
        # print(exhibIntro)
        exhibImg = response.xpath('//div[@class="v_news_content"]/p/img/@src').extract_first()
        if exhibImg != None:
            exhibImg = 'http://www.balujun.cn' + exhibImg
        # print(exhibImg)
        item['exhibImg'] = exhibImg
