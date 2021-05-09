import scrapy
from museum.items import collectionItem
import re
# scrapy crawl collection21

class Collection21Spider(scrapy.Spider):
    name = 'collection21'
    start_urls = ['http://www.bjqtm.com/dzzp/qtq/index.html']
    # start_urls = ['https://www.dpm.org.cn/collection//category_id/90/p/2.html']
    url = 'http://www.bjqtm.com/dzzp/qtq/index_%d.html'
    page_num = 2

    def parse_detail(self, response):
        item = response.meta["item"]
        coll_img = response.xpath('/html/body/div[4]/div/div[2]/div[2]/div[1]//img/@src').extract_first()
        coll_img = 'http://www.bjqtm.com' + coll_img
        print(coll_img)
        # if response.xpath('//*[@id="intro"]//text()'):
        coll_desc = response.xpath('/html/body/div[4]/div/div[2]/div[2]/div[1]//text()').extract()
        coll_desc = ''.join(coll_desc)
        print(coll_desc)
            
        # yield item

    def parse(self, response):
        item = collectionItem()
        coll_list = response.xpath('/html/body/div[4]/div/div[2]/div[2]/div[1]/ul/li')
        for li in coll_list:
            coll_name = li.xpath('./h2/text()').extract_first()
            print(coll_name)
            detail_url = 'http://www.bjqtm.com' + li.xpath('./a/@href').extract_first()
            print(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        
        if self.page_num <= 8:
            new_url = (self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)
