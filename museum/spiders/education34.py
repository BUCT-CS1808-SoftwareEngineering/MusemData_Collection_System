import scrapy
from museum.items import educationItem
import re 
import json
# scrapy crawl education34

class Education34Spider(scrapy.Spider):
    name = 'education34'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.qhmuseum.cn/qhm-webapi/api/v1/social/lectureAll?pageNumber=1&pageSize=10']

    def parse(self, response):
        item = educationItem()
        coll_list = json.loads(response.text)["data"]["list"]
        for i in coll_list:
            collectionName = i["title"]
            collectionName = ''.join(collectionName)
            collectionImageUrl = i["picture"]
            collectionImageUrl = ''.join(collectionImageUrl)
            # collectionDescription =  str(i["description"]) + "\n时间：" + str(i["display_time"]) + "\n地点：" + str(i["address"])
            print((collectionName, collectionImageUrl))
            # cont = "时间：" + str(i["display_time"]) + " 地点：" + str(i["address"])
            cont = str(i["contents"])
            cont = re.sub(r'<\/?.+?\/?>','',cont)
            print(cont)
            # yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})