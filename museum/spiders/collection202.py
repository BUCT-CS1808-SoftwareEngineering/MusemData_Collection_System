# -*- coding: utf-8 -*-
import scrapy


class LuxunSpider(scrapy.Spider):
    name = 'collection202'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.luxunmuseum.com.cn/guancangjingpin/']

    def parse_detail(self, response):
        # /html/body/div[3]/div[2]/div[2]/div[1]
        name = response.xpath('/html/body/div[3]/div[2]/div[2]/div[1]/text()').extract_first()
        # /html/body/div[3]/div[2]/div[2]/div[3]/p[2]
        # //*[@id="zoom"]/p[1]/img
        # /html/body/div[3]/div[2]/div[2]/div[3]/p[1]/img
        img = 'http://www.luxunmuseum.com.cn' + response.xpath('/html/body/div[3]/div[2]/div[2]/div[3]/p[3]/img[1]/@src | /html/body/div[3]/div[2]/div[2]/div[3]/p[1]/img/@src | //*[@id="zoom"]/p[1]/img/@src | /html/body/div[3]/div[2]/div[2]/div[3]/div[1]/img/@src | /html/body/div[3]/div[2]/div[2]/div[3]/p[2]/img/@src').extract_first()
        # /html/body/div[3]/div[2]/div[2]/div[3]/p[3]
        content = response.xpath('/html/body/div[3]/div[2]/div[2]/div[3]//text() | /html/body/div[3]/div[2]/div[2]/div[3]/div[2]//text() | /html/body/div[3]/div[2]/div[2]/div[3]/p[3]//text() |/html/body/div[3]/div[2]/div[2]/div[3]/table/tbody/tr/td//text()').extract()
        content = ''.join(content)
        print(name,img,content)

    def parse(self, response):
        dl_list = response.xpath('/html/body/div[3]/div[2]/div[2]/div[1]/dl')
        # print(dl_list)
        for i in dl_list:
            detail_url = 'http://www.luxunmuseum.com.cn' + i.xpath('./dt/div/a/@href').extract_first()
            # print(detail_url)
            yield scrapy.Request(detail_url, callback=self.parse_detail)

        if response.xpath('/html/body/div[3]/div[2]/div[2]/div[2]/p/a/@href').extract_first():
            next_page = 'http://www.luxunmuseum.com.cn' + response.xpath('/html/body/div[3]/div[2]/div[2]/div[2]/p/a/@href').extract_first()
            yield scrapy.Request(next_page, callback=self.parse)

# /html/body/div[3]/div[2]/div[2]/div[3]/p[2]/img