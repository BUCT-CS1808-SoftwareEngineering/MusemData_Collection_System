# -*- coding: utf-8 -*-
import scrapy
from museum.items import exhibitionItem


class Exhibition169Spider(scrapy.Spider):
    name = 'exhibition169'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.hljmuseum.com/clzl/jbcl/lscl/', 'http://www.hljmuseum.com/clzl/jbcl/lscl/',
                  'http://www.hljmuseum.com/clzl/jbcl/eqbwg/', 'http://www.hljmuseum.com/clzl/jbcl/yzxbxhcl/',
                  'http://www.hljmuseum.com/clzl/jbcl/dsmys/', 'http://www.hljmuseum.com/clzl/jbcl/fyxzfg/',
                  'http://www.hljmuseum.com/clzl/lszl/myyx/', 'http://www.hljmuseum.com/clzl/lszl/myyxian/',
                  'http://www.hljmuseum.com/clzl/lszl/mczl/', 'http://www.hljmuseum.com/clzl/lszl/hsjtz/',
                  'http://www.hljmuseum.com/clzl/lszl/yjzl/']

    def parse(self, response):
        li_list = response.xpath('//ul[@class="titlist04  f14"]/div/li')
        for li in li_list:
            item = exhibitionItem()
            exhibName = li.xpath('./a//text()').extract_first().strip()
            # print(exhibName)
            item['exhibName'] = exhibName
            url = 'http://www.hljmuseum.com' + li.xpath('./a/@href').extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc, meta={'item': item})

    def parse_desc(self, response):
        item = response.meta['item']
        exhibIntro = response.xpath('//div[@class="duanluo"]/p//text()').extract()
        exhibIntro = ''.join(exhibIntro).strip()
        item['exhibIntro'] = exhibIntro
        # print(exhibIntro)
        exhibImg = str(response.xpath('//div[@class="duanluo"]//img/@src').extract_first())
        if len(exhibImg) > 0 and exhibImg[0] != 'h':
            exhibImg = 'http://www.hljmuseum.com/' + exhibImg
        item['exhibImg'] = exhibImg
        # print(exhibImg)
