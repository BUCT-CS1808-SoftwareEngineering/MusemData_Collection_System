import scrapy
from museum.items import collectionItem
import json


class Collection71Spider(scrapy.Spider):
    name = 'collection71'
    url = 'https://www.gzchenjiaci.com/MYwebsite/rc/shuzg'
    

    def start_requests(self):
        form_data = {'page': '1',
                     'size': '50',
                     'articletype': '4',
                     'auditstatus': '2'}
        yield scrapy.FormRequest(self.url, callback=self.parse, formdata=form_data)

    def parse(self, response):
        item = collectionItem()
        coll_list = json.loads(response.text)["data"]
        for i in coll_list:
            collectionName = i["title"]
            collectionDescription = i["texture"]
            collectionImageUrl = "https://www.gzchenjiaci.com"+i["imgurl"]
            print((collectionName, collectionDescription, collectionImageUrl))
