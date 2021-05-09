import scrapy
from museum.items import educationItem 
import re
import json
# scrapy crawl education19

class Education19Spider(scrapy.Spider):
    name = 'education19'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.shanximuseum.com/sx/education/signup_list?offset=0&amount=5&_=1620562617668']

    def parse(self, response):
        item = educationItem()
        coll_list = json.loads(response.text)["data"]["list"]
        for i in coll_list:
            collectionName = i["title"]
            collectionName = ''.join(collectionName)
            collectionImageUrl = i["image"]
            collectionImageUrl = "http://www.shanximuseum.com" + ''.join(collectionImageUrl)
            # collectionDescription =  str(i["description"]) + "\n时间：" + str(i["display_time"]) + "\n地点：" + str(i["address"])
            print((collectionName, collectionImageUrl))
            cont = "时间：" + str(i["display_time"]) + " 地点：" + str(i["address"])
            print(cont)
            # yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
