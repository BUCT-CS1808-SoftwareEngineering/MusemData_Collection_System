import scrapy
from museum.items import collectionItem
from selenium import webdriver
import re
#scrapy crawl collection16
class Collection16Spider(scrapy.Spider):
    name = 'collection16'
    # allowed_domains = ['www.xxx.com']

    start_urls = ['https://www.tjbwg.com/cn/collection.aspx?TypeId=10929',
    'https://www.tjbwg.com/cn/collection.aspx?TypeId=10930',
    'https://www.tjbwg.com/cn/collection.aspx?TypeId=10931',
    'https://www.tjbwg.com/cn/collection.aspx?TypeId=10932',
    'https://www.tjbwg.com/cn/collection.aspx?TypeId=10933',
    'https://www.tjbwg.com/cn/collection.aspx?TypeId=10934']

    # url = 'http://www.njmuseumadmin.com/Antique/lists/p/%d'
    # cot = 0
    # page_num = 2
    # co_list = ['qtq','tq','yq','cq','sk','qt']
    # co_page = [10,8,3,4,1,2]

    def parse_detail(self, response):
        item = response.meta["item"]
        # coll_name = response.xpath('//*[@id="hl_content"]/div/div[2]/h3/span/text()').extract_first()
        # if response.xpath('//*[@id="doZoom"]//text()'):
        prim = response.xpath('/html/body/div/div[2]/div/div/div[2]/div[2]/div[1]/div[2]//text()').extract()
        
        # coll_desc = response.xpath('/html/body/div[1]/div[3]/div[2]/div/div[2]')
        # coll_desc = ''.join(coll_desc)
        # print(coll_desc)
        coll_desc = ''.join(prim)
        # coll_desc = re.sub(r'\s','',coll_desc)
        coll_desc = re.sub('&(.+?);','',coll_desc)
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
        coll_list = response.xpath('/html/body/div/div[3]/div/div/div[2]/div[2]/div/ul/li')
        for li in coll_list:
            # //*[@id="227613"]/text()
            coll_name = li.xpath('./div/a/h3/text()').extract_first()
            # coll_name = ''.join(coll_name)
            print(coll_name)
        # print(li.xpath('./td/a/@href').extract_first())
            detail_url = 'https://www.tjbwg.com/cn/' + li.xpath('./div/a/@href').extract_first()
            coll_img = li.xpath('./div/a/div/div[1]/img/@src').extract_first()
            coll_img = 'https://www.tjbwg.com' + coll_img
            print(coll_img)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
