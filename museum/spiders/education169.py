# -*- coding: utf-8 -*-
import scrapy


class Education169Spider(scrapy.Spider):
    name = 'education169'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.hljmuseum.com/bwgjy/lbjy/', 'http://www.hljmuseum.com/bwgjy/ldbwg/',
                  'http://www.hljmuseum.com/bwgjy/hqzrr/', 'http://www.hljmuseum.com/bwgjy/jjypx/',
                  'http://www.hljmuseum.com/bwgjy/zyzhd/']

    def parse(self, response):
        li_list = response.xpath('//ul[@class="titlist04  f14"]/div/li')
        for li in li_list:
            eduName = li.xpath('./a//text()').extract_first().strip()
            # print(eduName)
            url = 'http://www.hljmuseum.com' + li.xpath('./a/@href').extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc)

    def parse_desc(self, response):
        eduImg = response.xpath('//div[@class="duanluo"]//img/@src').extract_first()
        if eduImg != None:
            eduImg = 'http://www.hljmuseum.com' + eduImg
        # print(eduImg)
        eduContent = response.xpath('//div[@class="duanluo"]//p[@class="MsoNormal"]//text()').extract()
        eduContent = ''.join(eduContent).strip()
        # print(eduContent)
