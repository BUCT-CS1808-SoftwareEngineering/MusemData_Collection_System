# -*- coding: utf-8 -*-
import scrapy
from njmusePro.get_suburl import getsub
from njmusePro.items import collectionItem

class JsbwgSpider(scrapy.Spider):
    name = 'collection203'
    # allowed_domains = ['www.jb.mil.cn']
    start_urls = ['http://www.jb.mil.cn/gcww/wwjs_new/gjdww/']
    ww_list = ['tdgmsq/', 'krzzsq/', 'jfzzsq/', 'shzysq/']
    for i in ww_list:
        start_urls.append('http://www.jb.mil.cn/gcww/wwjs_new/'+i)

    def parse_detailp(self, response):
        item = response.meta['item']
        url = response.url
        url = getsub(url)
        img_url = url + response.xpath('/html/body/div[4]/div/div[1]/div/p[1]/img/@oldsrc | /html/body/div[4]/div/div[1]/div/p[1]/a/@oldsrc').extract_first()
        # img_url = response.xpath('/html/body/div[4]/div/div[1]/div/p[1]/a/@href')
        intro = response.xpath('/html/body/div[4]/div/div[1]/div/p[3]/text()').extract_first()
        # print(intro)
        print(img_url, intro)
        item['collectionIntroduction'] = intro
        item['collectionImage'] = img_url
        yield item

    def parse_detail(self, response):
        item = collectionItem()
        li_list = response.xpath('/html/body/div/div[1]/ul/li')
        # print(li_list)
        for i in li_list:
            detail_url = i.xpath('./a/@href').extract_first()
            # img_url = i.xpath('./a/img/@altonerror').extract_first()
            name = i.xpath('./a/span/text()').extract_first()
            item['collectionName'] = name
            # print(img_url)
            # print(detail_url, name)
            yield scrapy.Request(detail_url, callback=self.parse_detailp, meta={'item': item})
        if response.xpath('/html/body/div/div[2]/ul/a[@class = "next-page"]/@href').extract_first():
            next_url = 'http://www.jb.mil.cn/was/web/' + response.xpath('/html/body/div/div[2]/ul/a[@class = "next-page"]/@href').extract_first()
            yield scrapy.Request(next_url, callback=self.parse_detail)
        # for j in a_list:
        #     page_url = 'http://www.jb.mil.cn/was/web/' + j.xpath('./@href')

        #     yield scrapy.Request(page_url, callback=self.parse_detail)

    def parse(self, response):
        # li_list = response.xpath('/html/body/div/div[1]/ul/li')
        # print(li_list)
        # for i in li_list:
        #     detail_url = i.xpath('./a/@href').extract_first()
        #     img_url = i.xpath('./a/img/@src').extract_first()
        #     name = i.xpath('./a/span/text()').extract_first()
        #     print(detail_url, img_url, name)
        url = response.xpath('//*[@id="iframesrc"]/@src').extract_first()
        yield scrapy.Request(url, callback=self.parse_detail)
        # text = test.xpath('.//text()').extract_first()
        # print(text)
        # html = test[0].extract()
        # print(html)