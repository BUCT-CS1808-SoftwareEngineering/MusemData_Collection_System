# -*- coding: utf-8 -*-
import scrapy


class Education184Spider(scrapy.Spider):
    name = 'education184'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.balujun.cn/e/action/ShowInfo.php?classid=16&id=385',
                  'http://www.balujun.cn/e/action/ShowInfo.php?classid=16&id=384',
                  'http://www.balujun.cn/e/action/ShowInfo.php?classid=16&id=383',
                  'http://www.balujun.cn/e/action/ShowInfo.php?classid=16&id=382',
                  'http://www.balujun.cn/e/action/ShowInfo.php?classid=16&id=381']

    def parse(self, response):
        eduName = response.xpath('//div[@class="content-title"]/h3/text()').extract_first()
        # print(eduName)
        eduImg = response.xpath('//div[@class="v_news_content"]/div/img/@src').extract_first()
        if eduImg != None:
            eduImg = 'http://www.balujun.cn' + eduImg
        # print(eduImg)
        eduContent = response.xpath('//div[@class="v_news_content"]/div/p//text()').extract()
        eduContent = ''.join(eduContent).strip()
        # print(eduContent)
