import scrapy
from museum.items import collectionItem
import re
# scrapy crawl collection188

class Collection188Spider(scrapy.Spider):
    name = 'collection188'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://pjcmm.com/listPro.aspx?cateid=82']

    def parse_detail(self, response):
        item = response.meta["item"]
        name = response.xpath('//div[@class="contentTitle"]/text()').extract_first()
        print(name)
        # if response.xpath('//*[@id="intro"]//text()'):
        coll_desc = 'None'
        if response.xpath('/html/body/div[4]/div[2]/p//text()').extract():
            coll_desc = response.xpath('/html/body/div[4]/div[2]/p//text()').extract()
            coll_desc = ''.join(coll_desc)
        print(coll_desc)
            

    def parse(self, response):
        item = collectionItem()
        coll_list = response.xpath('/html/body/div[4]/div[2]/ul/li')
        for li in coll_list:
            img = "http://pjcmm.com" + li.xpath('./a/img/@src').extract_first()
            print(img)
            detail_url = "http://pjcmm.com/" + li.xpath('./a/@href').extract_first()
            print(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
