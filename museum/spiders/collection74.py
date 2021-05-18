import scrapy
from scrapy.http import headers
from museum.items import collectionItem
import json


class Collection74Spider(scrapy.Spider):
    name = 'collection74'
    start_urls = [
        'https://www.shenzhenmuseum.com/api/collection/page/L0302?lang=0&pageNum=1&pageSize=10000&platform=0&master=',
    ]
    api = "https://www.shenzhenmuseum.com/api/collection/get?clazzName=CmsCollection&platform=0&resId="
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62',
        'X-Req-platform': '0',
        'X-Requested-With': 'XMLHttpRequest'
    }

    def parse_content(self, response):
        item = collectionItem()
        collectionName = response.meta["name"]
        collectionDescription = json.loads(response.text)["data"]["detail"]
        collectionImageUrl = response.meta["image"]
        print((collectionName, collectionDescription, collectionImageUrl))

    def parse(self, response):
        coll_list = json.loads(response.text)["data"]["list"]
        for i in coll_list:
            meta = {
                "name": i["name"],
                "image": i["thumbPic"]
            }
            yield scrapy.Request(self.api+i['resId'], self.parse_content, headers=self.headers,meta=meta)
