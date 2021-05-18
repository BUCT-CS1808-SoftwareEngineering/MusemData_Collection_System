# -*- coding: utf-8 -*-
import scrapy
from njmusePro.items import exhibitionItem

class JsbwgzlSpider(scrapy.Spider):
    name = 'exhibition203'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.wmhg.com.cn/exhib/detail/55.html','https://www.wmhg.com.cn/exhib/detail/367.html','https://www.wmhg.com.cn/exhib/detail/267.html','https://www.wmhg.com.cn/exhib/detail/1353.html']

    def parse(self, response):
        item = exhibitionItem()
        title = response.xpath('/html/body/div[3]/div/div[1]/div/div/text()').extract_first()
        text = response.xpath('/html/body/div[3]/div/div[2]/div/div[2]/div//text()').extract()
        text = ''.join(text)
        # 图片动态加载，爬不到
        img_url = response.xpath('/html/body/div[3]/div/div[2]/div/div[1]/div[2]/div[2]/div/div[9]/div/div/img/@src').extract_first()
        print(text,img_url)
        item['exhibName'] = title
        item['exhibIntro'] = text
        item['exhibImg'] = img_url
        yield item
