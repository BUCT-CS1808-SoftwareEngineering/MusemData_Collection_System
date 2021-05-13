import scrapy
from museum.items import collectionItem
import json
from selenium import webdriver
# scrapy crawl collection38

class Collection38Spider(scrapy.Spider):
    name = 'collection38'
    start_urls = ['http://www.dtxsmuseum.com/news_pic_list.aspx?category_id=30&page=1']

    url = 'http://www.dtxsmuseum.com/news_pic_list.aspx?category_id=30&page=%d'
    page_num = 2

    def parse_detail(self, response):
        item = response.meta["item"]
        coll_desc = response.xpath('//*[@id="form1"]/div[4]/div[2]/div[4]//text()').extract()
        coll_desc = ''.join(coll_desc)
        print(coll_desc)
        # yield item

    def parse(self, response):
        item = collectionItem()
        coll_list = response.xpath('//*[@id="form1"]/div[4]/div[2]/ul/li')
        for li in coll_list:
            # if li.xpath('./td/a/text()').extract_first() != None:
            coll_name = li.xpath('./a/span[2]/text()').extract_first()
            # coll_name = ''.join(coll_name)
            print(coll_name)
            coll_img = "http://www.dtxsmuseum.com" + li.xpath('./a/span[1]/img/@src').extract_first()
            print(coll_img)
            detail_url = 'http://www.dtxsmuseum.com' + li.xpath('./a/@href').extract_first()
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
    
        if self.page_num <= 2:
            new_url = (self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)
