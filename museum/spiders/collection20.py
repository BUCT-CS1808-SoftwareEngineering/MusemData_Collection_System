import scrapy
from museum.items import collectionItem
import re
# scrapy crawl collection20
class Collection20Spider(scrapy.Spider):
    name = 'collection20'
    start_urls = ['http://www.gansumuseum.com/dc/list-58.html']
    # start_urls = ['https://www.dpm.org.cn/collection//category_id/90/p/2.html']
    url = 'http://www.gansumuseum.com/dc/list-58-%d.html'
    page_num = 2

    def parse_detail(self, response):
        item = response.meta["item"]
        # if response.xpath('//*[@id="intro"]//text()'):
        coll_desc = response.xpath('/html/body/div/div[2]/div[1]/div[2]/div[2]/div/div/div/div[3]//text()').extract()
        coll_desc = ''.join(coll_desc)
        print(coll_desc)
            
        # yield item

    def parse(self, response):
        item = collectionItem()
        coll_list = response.xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/ul/li')
        for li in coll_list:
            coll_name = li.xpath('./div/div/div[1]/label/text()').extract_first()
            print(coll_name)
            detail_url = 'http://www.gansumuseum.com' + li.xpath('./div/div/div[2]/a[2]/@href').extract_first()
            print(detail_url)
            coll_img = li.xpath('./div/a/img/@src').extract_first()
            coll_img = 'http://www.gansumuseum.com' + coll_img
            print(coll_img)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        
        if self.page_num <= 97:
            new_url = (self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)
