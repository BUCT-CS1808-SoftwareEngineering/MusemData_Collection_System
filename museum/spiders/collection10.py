import scrapy
from museum.items import collectionItem
import re
# import string
# scrapy crawl collection10

class Collection10Spider(scrapy.Spider):
    name = 'collection10'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.hongyan.info/list/35']

    url = 'https://www.hongyan.info/index/news_list/c_id/35/m/Home/p/%d.html'
    cot = 0
    page_num = 2
    # co_list = ['qtq','tq','yq','cq','sk','qt']
    # co_page = [10,8,3,4,1,2]

    def parse_detail(self, response):
        item = response.meta["item"]
        # coll_name = response.xpath('//*[@id="hl_content"]/div/div[2]/h3/span/text()').extract_first()
        # if response.xpath('//*[@id="doZoom"]//text()'):
        coll_desc = response.xpath('/html/body/div[7]/div[3]/div[3]/div[2]//text()').extract()
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
        coll_list = response.xpath('/html/body/div[8]/div[2]/div/div[@class = "product-list"]')
        print(coll_list)
        for div in coll_list:
            div_list = div.xpath('./div')
            for li in div_list:
            # //*[@id="227613"]/text()
                coll_name = li.xpath('./h2/a/text()').extract_first()
                # coll_name = ''.join(coll_name)
                print(coll_name)
            # print(li.xpath('./td/a/@href').extract_first())
                detail_url = 'https://www.hongyan.info' + li.xpath('./a/@href').extract_first()
                print(detail_url)
                coll_img = li.xpath('./a/img/@src').extract_first()
                coll_img = 'https://www.hongyan.info' + coll_img
                print(coll_img)
                yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        
        if self.page_num <= 3:
            # new_url = (self.url%(self.co_list[self.cot],self.page_num))
            new_url = (self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)
