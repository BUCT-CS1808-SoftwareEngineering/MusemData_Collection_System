# -*- coding: utf-8 -*-
import scrapy
from museum.items import exhibitionItem


class Exhibition180Spider(scrapy.Spider):
    name = 'exhibition180'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://neimenggubowuguan.meishujia.cn/?act=usite&said=368&usid=400']

    def parse(self, response):
        li_list = response.xpath('//dd[@class="theme_body_1231159117 theme_body_3751"]/ol/table[2]/tr/td/table')
        for li in li_list:
            item = exhibitionItem()
            exhibName = li.xpath('./tr[1]/td[2]/a/text()').extract_first().strip()
            # print(exhibName)
            item['exhibName'] = exhibName
            url = 'http://neimenggubowuguan.meishujia.cn/' + li.xpath('./tr[1]/td[2]/a/@href').extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc, meta={'item': item})

    def parse_desc(self, response):
        item = response.meta['item']
        exhibIntro = response.xpath('//ul[@class="zl_r_b zl_r_bt"]//text()').extract()
        exhibIntro = ''.join(exhibIntro).strip()
        item['exhibIntro'] = exhibIntro
        # print(exhibIntro)
        # exhibImg = response.xpath('//div[@class="DrawImagefox"]/img/@src').extract_first()
        # if exhibImg != None and exhibImg[0] != 'h':
        #     exhibImg = 'http://neimenggubowuguan.meishujia.cn' + exhibImg
        # print(exhibImg)
        exhibImg = None  # 这个博物馆的展览图片全都打不开
        item['exhibImg'] = exhibImg
