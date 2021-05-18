# -*- coding: utf-8 -*-
import scrapy


class BjzrzlSpider(scrapy.Spider):
    name = 'exhibition198'
    # allowed_domains = ['www.xxx.com']
    start_urls = []
    url = 'http://www.bmnh.org.cn/zljs/jbcl/{}/zljs/index.shtml'
    for i in range(1, 11):
        start_urls.append(url.format(i))

    def parse(self, response):
        name = response.xpath('/html/body/div[3]/div[2]/div[2]/p[1]/text()').extract_first()
        # content = response.xpath('/html/body/div[3]/div[2]/div[2]/div/p[2]/span/text()').extract_first()
        content = response.xpath('/html/body/div[3]/div[2]/div[2]/div//text()').extract()
        content = ''.join(content)
        img = 'http://www.bmnh.org.cn' + response.xpath('/html/body/div[3]/div[2]/div[2]/div/p[1]/img/@src').extract_first()
        print(name, content, img)
