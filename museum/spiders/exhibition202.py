# -*- coding: utf-8 -*-
import scrapy


class LuxunzlSpider(scrapy.Spider):
    name = 'exhibition202'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.luxunmuseum.com.cn/zuixinzhanlan/']

    def parse_detail(self, response):
        title = response.xpath('/html/body/div[3]/div[2]/div[2]/div[1]/text()').extract_first()
        img = 'http://www.luxunmuseum.com.cn' + response.xpath('/html/body/div[3]/div[2]/div[2]/div[3]/p[5]/img/@src | /html/body/div[3]/div[2]/div[2]/div[3]/p[4]/img/@src').extract_first()
        content = response.xpath('/html/body/div[3]/div[2]/div[2]/div[3]//text()').extract()
        content = ''.join(content)
        print(title, img, content)

    def parse(self, response):
        div_list = response.xpath('/html/body/div[3]/div[2]/div[2]/div[1]/div')
        for i in div_list:
            # print(i)
            detail_url = 'http://www.luxunmuseum.com.cn' + i.xpath('./div/a/@href').extract_first()
            yield scrapy.Request(detail_url, callback=self.parse_detail)