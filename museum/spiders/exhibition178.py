# -*- coding: utf-8 -*-
import scrapy
from museum.items import exhibitionItem


class Exhibition178Spider(scrapy.Spider):
    name = 'exhibition178'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://ordosbwg.org.cn/zlcl_121914/lszl/202004/t20200427_2627867.html',
                  'http://ordosbwg.org.cn/zlcl_121914/lszl/202004/t20200427_2627860.html',
                  'http://ordosbwg.org.cn/zlcl_121914/lszl/202004/t20200427_2627853.html',
                  'http://ordosbwg.org.cn/zxdt_121912/201909/t20190905_2450836.html']

    def parse(self, response):
        item = exhibitionItem()
        exhibName = response.xpath('.//div[@class="details"]/h1/text()').extract_first().strip()
        # print(exhibName)
        item['exhibName'] = exhibName
        exhibIntro = response.xpath('//div[@class="TRS_Editor"]//p/text()').extract()
        exhibIntro = ''.join(exhibIntro).strip()
        item['exhibIntro'] = exhibIntro
        # print(exhibIntro)
        exhibImg = list(response.xpath('//div[@class="TRS_Editor"]//p/img/@src').extract_first())[1:]
        exhibImg = ''.join(exhibImg)
        pre_url = list(response.url)[:-23]
        pre_url = ''.join(pre_url)
        exhibImg = pre_url + exhibImg
        # print(exhibImg)
        item['exhibImg'] = exhibImg
