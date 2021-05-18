import scrapy
from museum.items import collectionItem
import re
# scrapy crawl collection193

class Collection193Spider(scrapy.Spider):
    name = 'collection193'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.printingmuseum.cn/Collection/List/CPZL?subNo=qt&pno=YSJP&page=1&X-Requested-With=XMLHttpRequest']
    url = "http://www.printingmuseum.cn/Collection/List/CPZL?subNo=qt&pno=YSJP&page=%d&X-Requested-With=XMLHttpRequest"
    num = 2

    # def parse_detail(self, response):
    #     item = response.meta["item"]
    #     name = response.xpath('//div[@class="contentTitle"]/text()').extract_first()
    #     print(name)
    #     # if response.xpath('//*[@id="intro"]//text()'):
    #     coll_desc = 'None'
    #     if response.xpath('/html/body/div[4]/div[2]/p//text()').extract():
    #         coll_desc = response.xpath('/html/body/div[4]/div[2]/p//text()').extract()
    #         coll_desc = ''.join(coll_desc)
    #     print(coll_desc)
            

    def parse(self, response):
        item = collectionItem()
        coll_list = response.xpath('//ul[@id="ulImgList"]/li')
        for li in coll_list:
            if li.xpath('./a/p/text()').extract_first():
                img =li.xpath('./a/img/@src').extract_first()
                print(img)
                name = li.xpath('./a/@title').extract_first()
                print(name)
                cont = '暂无'
                print(cont)
                # detail_url = "http://pjcmm.com/" + li.xpath('./a/@href').extract_first()
                # print(detail_url)
                # yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        
        if self.num <= 97:
            new_url = (self.url%self.num)
            self.num += 1
            yield scrapy.Request(new_url,callback=self.parse)

