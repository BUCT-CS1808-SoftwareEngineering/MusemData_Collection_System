import scrapy
from museum.items import collectionItem
import re
# import string
# scrapy crawl collection9
class Collection9Spider(scrapy.Spider):
    name = 'collection9'
    start_urls = ['http://www.chnmus.net/sitesources/hnsbwy/page_pc/dzjp/zpjc/qtq/list1.html']
    # start_urls = ['https://www.dpm.org.cn/collection//category_id/90/p/2.html']
    url = 'http://www.chnmus.net/sitesources/hnsbwy/page_pc/dzjp/zpjc/qtq/list%d.html'
    cot = 0
    page_num = 2
    # co_list = ['qtq','tq','yq','cq','sk','qt']
    # co_page = [10,8,3,4,1,2]

    def parse_detail(self, response):
        item = response.meta["item"]
        # coll_name = response.xpath('//*[@id="hl_content"]/div/div[2]/h3/span/text()').extract_first()
        if response.xpath('//*[@id="doZoom"]//text()'):
            coll_desc = response.xpath('//*[@id="doZoom"]//text()').extract()
            coll_desc = ''.join(coll_desc)
           
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
        coll_list = response.xpath('//*[@id="articleListTable"]/ul/li')
        for li in coll_list:
            # //*[@id="227613"]/text()
            coll_name = li.xpath('./a/h5/text()').extract_first()
            # coll_name = ''.join(coll_name)
            print(coll_name)
        # print(li.xpath('./td/a/@href').extract_first())
            detail_url = 'http://www.chnmus.net' + li.xpath('./a/@href').extract_first()
            coll_img = li.xpath('./a/img/@src').extract_first()
            coll_img = 'http://www.chnmus.net' + coll_img
            print(coll_img)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        
        if self.page_num <= 10:
            # new_url = (self.url%(self.co_list[self.cot],self.page_num))
            new_url = (self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)

        
        # self.page_num = 2
        # self.cot += 1
