import scrapy
from museum.items import collectionItem
import json


class Collection44Spider(scrapy.Spider):
    name = 'collection44'

    def start_requests(self):
        url = "http://www.tibetmuseum.com.cn//api/exhibit/exhibit_list?p=w&language=1&skip=0&take=6&class="
        for i in range(1,10):
            yield scrapy.Request(url+str(i))

    def parse(self, response):
        item = collectionItem()
        coll_list = json.loads(response.text)['data']['exhibit_list']
        for i in coll_list:
            collectionName = i["title"]
            collectionDescription = scrapy.Selector(text=i["content"]).xpath('//text()').get()
            collectionImageUrl = "http://www.tibetmuseum.com.cn/"+i["list_img"]
            print((collectionName, collectionDescription, collectionImageUrl))
