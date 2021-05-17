import scrapy
#scrapy crawl collection
#scrapy crawl exhiition
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
from museum.items import collectionItem
import json

class Collection122Spider(scrapy.Spider):
    name = 'collection141'
    #allowed_domains = ['www.ccc.com']
    start_urls = ['https://www.zsbwg.com/zhoushan1/man/antique?pageNumber=1&pageSize=12&fengpinfeilei=8a7aef0958b37e280158b38d781e0033']
    page_num=2
    url='https://www.zsbwg.com/zhoushan1/man/antique?pageNumber=%d&pageSize=12&fengpinfeilei=8a7aef0958b37e280158b38d781e0033'
    def parse(self, response):
        item = collectionItem()
        #scrapy crawl collection141
        _list = json.loads(response.text)["paginate"]["list"]
        for li in _list:
            coll_name=li["title"]
            coll_img=li["thumb"]
            detail_url='https://www.zsbwg.com/zhoushan1/vol/antique?catid=61&id=~'
            t=str(li["id"])
            detail_url=detail_url.replace('~',t,2)
            print(coll_name)
            print(coll_img)
            print(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
            #scrapy crawl collection141
        if self.page_num <= 78:
            new_url = (self.url%(self.page_num))
            print(new_url)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)
    def parse_detail(self,response):
        x=json.loads(response.text)["list"]
        for li in x:
            coll_desc=li["Cangpinmiaoshu"]
            print(coll_desc)
            break

