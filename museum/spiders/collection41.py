import scrapy
from museum.items import collectionItem
import json
# import string
# scrapy crawl collection9


class Collection41Spider(scrapy.Spider):
    name = 'collection41'
    start_urls = [
        'https://www.xabwy.com/api/website/article/list?&currentPage=1&pageSize=1000&typeId=190',
        'https://www.xabwy.com/api/website/article/list?&currentPage=1&pageSize=1000&typeId=191',
        'https://www.xabwy.com/api/website/article/list?&currentPage=1&pageSize=1000&typeId=192',
        'https://www.xabwy.com/api/website/article/list?&currentPage=1&pageSize=1000&typeId=193',
        'https://www.xabwy.com/api/website/article/list?&currentPage=1&pageSize=1000&typeId=194',
        'https://www.xabwy.com/api/website/article/list?&currentPage=1&pageSize=1000&typeId=195',
        'https://www.xabwy.com/api/website/article/list?&currentPage=1&pageSize=1000&typeId=196',
        'https://www.xabwy.com/api/website/article/list?&currentPage=1&pageSize=1000&typeId=197',
    ]

    def parse(self, response):
        item = collectionItem()
        coll_list = json.loads(response.text)["body"]["list"]
        for i in coll_list:
            collectionName = i["title"]
            collectionDescription = i["description"]
            collectionImageUrl = i["litPic"]
            print((collectionName, collectionDescription, collectionImageUrl))
