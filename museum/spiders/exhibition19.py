import scrapy
from museum.items import exhibitionItem 
import re
import json
# scrapy crawl exhibition19
class Exhibition19Spider(scrapy.Spider):
    name = 'exhibition19'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.shanximuseum.com/sx/exhibition/temporary_list?offset=0&count=6&year=&keyword=&_=1620549463272']

    def parse(self, response):
        item = exhibitionItem()
        coll_list = json.loads(response.text)["data"]["list"]
        for i in coll_list:
            collectionName = i["title"]
            collectionName = ''.join(collectionName)
            collectionImageUrl = i["image"]
            collectionImageUrl = "http://www.shanximuseum.com" + ''.join(collectionImageUrl)
            # detail_url = i["fullurl"]
            # detail_url = ''.join(detail_url)
            # print(detail_url)
            collectionDescription =  str(i["description"]) + "\n时间：" + str(i["display_time"]) + "\n地点：" + str(i["address"])
            # collectionDescription = ''.join(collectionDescription)
            # collectionImageUrl = 'http://www.njmuseum.com' + ''.join(collectionImageUrl)
            print((collectionName, collectionImageUrl))
            print(collectionDescription)
