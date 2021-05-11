import scrapy
from museum.items import collectionItem
import re
# scrapy crawl collection31

class Collection31Spider(scrapy.Spider):
    name = 'collection31'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.nxgybwg.com/e/action/ListInfo/index.php?page=0&classid=17']
    url = 'http://www.nxgybwg.com/e/action/ListInfo/index.php?page=%d&classid=17'
    page_num = 1

    def parse_detail(self, response):
        item = response.meta["item"]
        # if response.xpath('//*[@id="intro"]//text()'):
        coll_desc = 'None'
        if response.xpath('//*[@id="body_wrap"]/div/div[2]/div[2]/div/div[2]/div//text()').extract():
            coll_desc = response.xpath('//*[@id="body_wrap"]/div/div[2]/div[2]/div/div[2]/div//text()').extract()
            coll_desc = ''.join(coll_desc)
        print(coll_desc)
            

    def parse(self, response):
        item = collectionItem()
        coll_list = response.xpath('//*[@id="body_wrap"]/div/div[2]/div[2]/div[2]/ul/li')
        for li in coll_list:
            name = li.xpath('./p/a/text()').extract_first()
            print(name)
            img = li.xpath('./div/a/img/@src').extract_first()
            print(img)
            detail_url = "http://www.nxgybwg.com" + li.xpath('./div/a/@href').extract_first()
            print(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        
        if self.page_num <= 3:
            new_url = (self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)
