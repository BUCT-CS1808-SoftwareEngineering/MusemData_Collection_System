import scrapy
from museum.items import collectionItem
import re
# scrapy crawl collection11

class Collection11Spider(scrapy.Spider):
    name = 'collection11'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.19371213.com.cn/collection/featured/index_16685_1.html?_=1620443060130']
    url = 'http://www.19371213.com.cn/collection/featured/index_16685_%d.html?_=1620443060130'
    page_num = 2

    def parse_detail(self, response):
        item = response.meta["item"]
        coll_name = response.xpath('//*[@id="node-3388"]/section/div[2]/header/h4/text()').extract_first()
        # coll_name = ''.join(coll_name)
        print(coll_name)
        cont = 'None'
        print(cont)
        # coll_name = response.xpath('//*[@id="hl_content"]/div/div[2]/h3/span/text()').extract_first()
        # coll_desc = response.xpath('//*[@id="hl_content"]/div/div[2]/div[1]/div[1]/p/text()').extract()
        # coll_desc = ''.join(coll_desc)
        # coll_img = response.xpath('//*[@id="hl_content"]/div/div[1]/div/div/div/img/@src').extract_first()
        # # print(coll_name)
        # print(coll_desc)
        # print(coll_img)
        # yield item

    def parse(self, response):
        item = collectionItem()
        # //*[@id="building2"]/div/div[2]/table/tbody
        coll_list = response.xpath('/html/body/div')
        for li in coll_list:
            # if li.xpath('./td/a/text()').extract_first() != None:
                # //*[@id="227613"]/text()
            # coll_name = li.xpath('./td/a/text()').extract_first()
            # # coll_name = ''.join(coll_name)
            # print(coll_name)
            # print(li.xpath('./td/a/@href').extract_first())
            img_new = li.xpath('./section/div[1]/div/a/img/@src').extract_first()
            img_new = img_new.replace(".",'',2)
            img = "http://www.19371213.com.cn/collection" + img_new
            print(img)
            url_new = li.xpath('./section/div[1]/div/a/@href').extract_first()
            url_new = url_new.replace(".",'',2)
            detail_url = "http://www.19371213.com.cn/collection" + url_new
            # detail_url = 'https://www.dpm.org.cn/' + li.xpath('./td/a/@href').extract_first()
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        
        if self.page_num <= 17:
            new_url = (self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)
        
