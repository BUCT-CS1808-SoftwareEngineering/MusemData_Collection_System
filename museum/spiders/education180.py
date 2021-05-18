# -*- coding: utf-8 -*-
import scrapy


class Education180Spider(scrapy.Spider):
    name = 'education180'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://neimenggubowuguan.meishujia.cn/?act=usite&said=357&usid=400']

    def parse(self, response):
        li_list = response.xpath('//dd[@class="theme_body_1231159117 theme_body_3716"]/ol/table[2]/tr/td[2]/span')
        for li in li_list:
            eduName = li.xpath('./a/text()').extract_first()
            if eduName == None:
                continue
            # print(eduName)
            url = 'http://neimenggubowuguan.meishujia.cn' + li.xpath('./a/@href').extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc)

    def parse_desc(self, response):
        eduImg = None  # 这个博物馆的展览图片全都打不开
        # print(eduImg)
        eduContent = response.xpath('//ul[@class="pl_r_b pl_r_bt"]//text()').extract()
        if eduContent != None:
            eduContent = ''.join(eduContent).strip()
        # print(eduContent)
