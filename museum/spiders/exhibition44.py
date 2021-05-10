import scrapy
from museum.items import exhibitionItem
import json


class Exhibition44Spider(scrapy.Spider):
    name = 'exhibition44'
    start_urls = ["http://www.tibetmuseum.com.cn//api/exhibition/index?p=w&language=1"]

    def parse(self, response):
        item = exhibitionItem()
        coll_list = json.loads(response.text)['data']['zhuanti']
        for i in coll_list:
            exhibitionName = i["title"]
            exhibitionDescription = i["theme"]
            exhibitionImageUrl = "http://www.tibetmuseum.com.cn/"+i["list_img"]
            print((exhibitionName, exhibitionImageUrl, exhibitionDescription))
