import scrapy
from museum.items import collectionItem
import json


class Collection63Spider(scrapy.Spider):
    name = 'collection63'
    url = 'http://www.hainanmuseum.org/hnbwgcms/hnswb/api/cultural/list/api?pagesize='


    def start_requests(self):
        for id in range(100,10000,100):
            yield scrapy.Request(f"{self.url}{id}&start=1",callback=self.parse)

    def parse(self, response):
        item = collectionItem()
        coll_list = json.loads(response.text)["data"]["data"]
        for i in coll_list:
            collectionName = i["mingchen"]
            collectionDescription = i["niandai"]+" "+i["leibie"]+" "+i["chicun"]+" "+i["baocun_zhuangtai"]
            collectionImageUrl = "http://www.hainanmuseum.org/cms/1/image/public/wenwu/"+i["pics"][0]+".png"
            print((collectionName, collectionDescription, collectionImageUrl))
