# -*- coding: utf-8 -*-
import scrapy
from njmusePro.items import educationItem

class JsbwgjySpider(scrapy.Spider):
    name = 'education203'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.wmhg.com.cn/news_activity.html']

    def parse_detail(self, response):
        item = response.meta['item']
        # content = response.xpath('/html/body/div[4]/div/div[2]/div/div/div//text()').extract()
        # content = ''.join(content)
        title = response.xpath('/html/body/div[4]/div/div[1]/div/div/text()').extract_first()
        # print(title, content)
        # print(title)
        item['eduName'] = title
        yield item

    def parse(self, response):
        div_list = response.xpath('//*[@id="datalist"]/div[1]/div')
        item = educationItem()
        for i in div_list:
            detail_url = 'https://www.wmhg.com.cn' + i.xpath('./div[1]/a/@href').extract_first()
            img_url = 'https://www.wmhg.com.cn/' + i.xpath('./div[1]/a/img/@src').extract_first()
            intro = i.xpath('./div[2]/div[2]//text()').extract_first()
            # print(detail_url, img_url, intro)
            item['eduUrl'] = detail_url
            item['eduContent'] = intro
            item['eduImg'] = img_url
            yield scrapy.Request(detail_url, callback=self.parse_detail, meta={'item': item})


