# -*- coding: utf-8 -*-
import scrapy


class LuxunjySpider(scrapy.Spider):
    name = 'education202'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.luxunmuseum.com.cn/jiaoyuhuodongjieshao/']

    def parse_detail(self, response):
        title = response.xpath('/html/body/div[3]/div[2]/div[2]/div[1]/text()').extract_first()
        if response.xpath('/html/body/div[3]/div[2]/div[2]/div[3]/p[12]/img/@src').extract_first():
            img = 'http://www.luxunmuseum.com.cn' + response.xpath('/html/body/div[3]/div[2]/div[2]/div[3]/p[12]/img/@src').extract_first()
        else:
            img = None
        content = response.xpath('/html/body/div[3]/div[2]/div[2]/div[3]//text()').extract()
        print(title, img, content)

    def parse(self, response):
        div_list = response.xpath('/html/body/div[3]/div[2]/div[2]/div[1]/div')
        for i in div_list:
            detail_url = 'http://www.luxunmuseum.com.cn/' + i.xpath('./div[2]/a/@href').extract_first()
            yield scrapy.Request(detail_url, callback=self.parse_detail)
