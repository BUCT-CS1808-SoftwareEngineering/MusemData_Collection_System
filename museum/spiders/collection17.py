import scrapy
from selenium import webdriver
from museum.items import collectionItem
import json
# scrapy crawl collection17
class Collection17Spider(scrapy.Spider):
    name = 'collection17'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.3gmuseum.cn/web/cultural/findCulturalPage.do?pageSize=5000&pageNumber=1&itemno=4028808a5e3b12de015e3b2c79340003&type=&level=&years=&name=&byType=']

    def parse(self, response):
        item = collectionItem()
        coll_list = json.loads(response.text)["list"]
        for i in coll_list:
            collectionName = i["name"]
            collectionName = ''.join(collectionName)
            collectionImageUrl = i["picurl"]
            collectionImageUrl = ''.join(collectionImageUrl)
            collectionDescription = "\n文物类型：" + str(i["type"]) + "\n文物级别：" + str(i["level"]) + "\n完残程度：" + str(i["residuegrade"]) + "\n具体尺寸(cm)：" + str(i["size"])
            # collectionDescription = ''.join(collectionDescription)
            # collectionImageUrl = 'http://www.njmuseum.com' + ''.join(collectionImageUrl)
            print((collectionName, collectionDescription, collectionImageUrl))
