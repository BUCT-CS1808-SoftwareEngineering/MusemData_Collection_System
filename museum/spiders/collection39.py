import scrapy
from museum.items import collectionItem
import json
from selenium import webdriver
# scrapy crawl collection39

class Collection39Spider(scrapy.Spider):
    name = 'collection39'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.yagmjng.com/rsf/site/jinianguan/wenwujianshang/index.html']

    url = 'http://www.yagmjng.com/rsf/site/jinianguan/wenwujianshang/index_%d.html'
    page_num = 1

    # def parse_detail(self, response):
    #     item = response.meta["item"]
    #     # coll_name = response.xpath('//*[@id="hl_content"]/div/div[2]/h3/span/text()').extract_first()
    #     coll_desc = response.xpath('//*[@id="hl_content"]/div/div[2]/div[1]/div[1]/p/text()').extract()
    #     coll_desc = ''.join(coll_desc)
    #     print(coll_desc)
    #     # yield item

    def parse(self, response):
        item = collectionItem()
        coll_list = response.xpath('//*[@id="middle"]/div[2]/div[2]/div/div[2]/div')
        for li in coll_list:
            if li.xpath('./div[2]/a/text()').extract_first() != None:
                coll_name = li.xpath('./div[2]/a/text()').extract_first()
                # coll_name = ''.join(coll_name)
                print(coll_name)
                coll_img = "http://www.yagmjng.com" + li.xpath('./div[1]/a/img/@src').extract_first()
                print(coll_img)
                detail_url = 'http://www.yagmjng.com' + li.xpath('./div[1]/a/@href').extract_first()
                cont = "暂无"
                print(cont)
                # yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        
        if self.page_num <= 2:
            new_url = (self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)