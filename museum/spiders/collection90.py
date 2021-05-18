import scrapy
from museum.items import collectionItem
import json

class Collection90Spider(scrapy.Spider):
    name = 'collection90'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.hbww.org/ashx/ajax.ashx?type=Archives&channelNo=QT&page=1&PageSize=1000&fldSort=PublishDate&Sort=1&rnd=0.42563924516552043']
                  
    def parse(self, response):
        item = collectionItem()
        coll_list = json.loads(response.text)["Rows"]
        for i in coll_list:
            coll_name = i["Title"]
            coll_desc = i["Contents"]
            #coll_img = i[""]
            print(coll_name)
            print(coll_desc)

