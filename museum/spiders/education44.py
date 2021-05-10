import scrapy
from museum.items import educationItem
import json


class Education44Spider(scrapy.Spider):
    name = 'education44'
    start_urls = ["http://39.106.176.234//api/activity/index?p=w&language=1"]

    def parse(self, response):
        item = educationItem()
        coll_list = json.loads(response.text)['data']['old_list']
        for i in coll_list:
            educationName = i["title"]
            educationDescription = i["brief_desc"]
            educationImageUrl = "http://www.tibetmuseum.com.cn/"+i["list_img"]
            print((educationName, educationImageUrl, educationDescription))
