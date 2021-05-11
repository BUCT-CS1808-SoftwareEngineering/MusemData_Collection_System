import scrapy
from museum.items import collectionItem
import re
# scrapy crawl collection32

class Collection32Spider(scrapy.Spider):
    name = 'collection32'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.nxbwg.com/c/jpww.html']

    def parse_detail(self, response):
        item = response.meta["item"]
        # if response.xpath('//*[@id="intro"]//text()'):
        coll_desc = 'None'
        if response.xpath('//*[@id="content-container"]/div/main/div/div[2]/div[2]//text()').extract():
            coll_desc = response.xpath('//*[@id="content-container"]/div/main/div/div[2]/div[2]//text()').extract()
            coll_desc = ''.join(coll_desc)
        print(coll_desc)
            

    def parse(self, response):
        item = collectionItem()
        coll_list = response.xpath('//*[@id="pb-box"]/div')
        for li in coll_list:
            if li.xpath('./h3/a/text()').extract_first():
                name = li.xpath('./h3/a/text()').extract_first()
                print(name)
                img = li.xpath('./a/div/img/@src').extract_first()
                print(img)
                detail_url = "http://www.nxbwg.com" + li.xpath('./a/@href').extract_first()
                print(detail_url)
                yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
