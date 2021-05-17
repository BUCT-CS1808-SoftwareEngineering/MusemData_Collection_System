import scrapy
from museum.items import exhibitionItem
import json


class Exhibition78Spider(scrapy.Spider):
    name = 'exhibition78'
    start_urls = [
        'https://www.csm.hn.cn/museum/spexpo/listSpexpo.shtml?pageSize=5&type=3&pageIndex=1&title=&year=&noCatch=1621261249000',
    ]

    def parse(self, response):
        item = exhibitionItem()
        coll_list = json.loads(response.text)["data"]["recordsList"]
        for i in coll_list:
            educationName = i["title"]
            educationDescription = i["content"]
            educationImageUrl = i["mainPicUrl"]
            print((educationName, educationDescription, educationImageUrl))
