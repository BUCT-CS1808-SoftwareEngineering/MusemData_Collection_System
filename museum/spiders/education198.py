# -*- coding: utf-8 -*-
import scrapy


class BjzrjySpider(scrapy.Spider):
    name = 'education198'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.bmnh.org.cn/jyhd/hdjs/16/index.shtml','http://www.bmnh.org.cn/jyhd/hdjs/4/index.shtml','http://www.bmnh.org.cn/jyhd/hdjs/17/index.shtml','http://www.bmnh.org.cn/jyhd/hdjs/5/index.shtml']

    def parse(self, response):
        name = response.xpath('/html/body/div[3]/div[1]/p/span/a/text()').extract_first()
        img = 'http://www.bmnh.org.cn' + response.xpath('/html/body/div[3]/div[2]/div[2]/div[2]/div[1]/img/@src').extract_first()
        content = response.xpath('/html/body/div[3]/div[2]/div[2]/div[2]/div[1]//text()').extract()
        content = ''.join(content)
        print(name, img, content)
