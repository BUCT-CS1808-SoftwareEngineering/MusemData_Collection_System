import scrapy
from museum.items import collectionItem
import json


class Collection78Spider(scrapy.Spider):
    name = 'collection78'
    start_urls = [
        'https://www.csm.hn.cn/museum/collection/listCollection.shtml?collectionType=3&pageSize=1000',
        'https://www.csm.hn.cn/museum/collection/listCollection.shtml?collectionType=6&pageSize=1000',
        'https://www.csm.hn.cn/museum/collection/listCollection.shtml?collectionType=7&pageSize=1000',
        'https://www.csm.hn.cn/museum/collection/listCollection.shtml?collectionType=18&pageSize=1000',
        'https://www.csm.hn.cn/museum/collection/listCollection.shtml?collectionType=20&pageSize=1000',
        'https://www.csm.hn.cn/museum/collection/listCollection.shtml?collectionType=21&pageSize=1000',
        'https://www.csm.hn.cn/museum/collection/listCollection.shtml?collectionType=26&pageSize=1000'
    ]

    def parse(self, response):
        item = collectionItem()
        coll_list = json.loads(response.text)["data"]["recordsList"]
        for i in coll_list:
            collectionName = i["name"]
            collectionDescription = i["introduce"]
            collectionImageUrl = i["picUrl"]
            print((collectionName, collectionDescription, collectionImageUrl))
