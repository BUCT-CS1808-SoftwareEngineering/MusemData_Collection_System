import scrapy
from museum.items import collectionItem
import json

class Collection89Spider(scrapy.Spider):
    name = 'collection89'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.whmuseum.com.cn/japi/sw-cms/api/queryExhibitList']

    def parse(self, response):
        item = collectionItem()
        coll_list = json.loads(response.text)["data"]["records"]
        for i in coll_list:
            coll_name = i["exhibitName"]
            coll_desc = i["description"]
            #coll_img = i[""]
            print((coll_name, coll_desc))
