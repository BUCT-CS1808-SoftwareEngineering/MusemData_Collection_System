import scrapy
from museum.items import exhibitionItem
import json


class Exhibition90Spider(scrapy.Spider):
    name = 'exhibition90'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.hbww.org/ashx/ajax.ashx?type=Archives&channelNo=LSZL&page=1&PageSize=1000&fldSort=PublishDate&Sort=1&rnd=0.4120991922312366']

    def parse(self, response):
        item = exhibitionItem()
        coll_list = json.loads(response.text)["Rows"]
        for i in coll_list:
            coll_name = i["Title"]
            coll_desc = i["Contents"]
            #coll_img = i[""]
            print(coll_name)
            print(coll_desc)
