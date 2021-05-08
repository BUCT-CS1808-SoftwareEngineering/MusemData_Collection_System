import scrapy
from museum.items import collectionItem
from selenium import webdriver
import re
#scrapy crawl collection15

class Collection15Spider(scrapy.Spider):
    name = 'collection15'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.njmuseumadmin.com/Antique/lists/p/1']

    url = 'http://www.njmuseumadmin.com/Antique/lists/p/%d'
    cot = 0
    page_num = 2
    # co_list = ['qtq','tq','yq','cq','sk','qt']
    # co_page = [10,8,3,4,1,2]

    def parse_detail(self, response):
        item = response.meta["item"]
        # coll_name = response.xpath('//*[@id="hl_content"]/div/div[2]/h3/span/text()').extract_first()
        # if response.xpath('//*[@id="doZoom"]//text()'):
        prim = response.xpath('//*[@id="DB_gallery"]/div[2]/div[2]//text()').extract()
        
        # coll_desc = response.xpath('/html/body/div[1]/div[3]/div[2]/div/div[2]')
        # coll_desc = ''.join(coll_desc)
        # print(coll_desc)
        coll_desc = ''.join(prim)
        coll_desc = re.sub(r'\s','',coll_desc)
        # print(coll_name)
        print(coll_desc)
            
        # yield item

    def parse(self, response):
        item = collectionItem()
        # maxn = response.xpath('//*[@class="active"]/text()').extract_first()
        # maxn = ''.join(maxn)
        # maxn = int(maxn)
        # //*[@id="building2"]/div/div[2]/table/tbody
        # if maxn == '1':
        #     self.cot += 1
        coll_list = response.xpath('//*[@id="form"]/div[3]/div[2]/ul/li')
        for li in coll_list:
            # //*[@id="227613"]/text()
            coll_name = li.xpath('./a/span/text()').extract_first()
            # coll_name = ''.join(coll_name)
            print(coll_name)
        # print(li.xpath('./td/a/@href').extract_first())
            detail_url = 'http://www.njmuseumadmin.com' + li.xpath('./a/@href').extract_first()
            coll_img = li.xpath('./a/img/@src').extract_first()
            coll_img = 'http://www.njmuseumadmin.com' + coll_img
            print(coll_img)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        
        if self.page_num <= 12:
            # new_url = (self.url%(self.co_list[self.cot],self.page_num))
            new_url = (self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)
