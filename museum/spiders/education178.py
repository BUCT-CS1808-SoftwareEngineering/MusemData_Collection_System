# -*- coding: utf-8 -*-
import scrapy


class Education178Spider(scrapy.Spider):
    name = 'education178'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://ordosbwg.org.cn/xsyj_121935/lsyj/']

    def parse(self, response):
        li_list = response.xpath('//div[@class="history-list-msg"]/ul/li')
        for li in li_list:
            eduName = li.xpath('./span/a/text()').extract_first().strip()
            # print(eduName)
            url = list(li.xpath('./span/a/@href').extract_first())[1:]
            url = ''.join(url)
            url = 'http://ordosbwg.org.cn/xsyj_121935/lsyj' + url
            # print(url)
            yield scrapy.Request(url, callback=self.parse_desc)

    def parse_desc(self, response):
        eduImg = response.xpath('//div[@class="TRS_Editor"]/div/p/img/@src').extract_first()
        if eduImg != None:
            eduImg = list(eduImg)[1:]
            eduImg = ''.join(eduImg)
            pre_url = list(response.url)[:-23]
            pre_url = ''.join(pre_url)
            eduImg = pre_url + eduImg
        # print(eduImg)
        eduContent = response.xpath('//div[@class="TRS_Editor"]//text()').extract()
        eduContent = ''.join(eduContent).strip()
        # print(eduContent)
