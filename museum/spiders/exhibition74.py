import scrapy
from museum.items import exhibitionItem
import json


class Exhibition74Spider(scrapy.Spider):
    name = 'exhibition74'
    start_urls = [
        'https://www.shenzhenmuseum.com/api/exhibition/page/L0202?lang=0&pageNo=1&pageSize=999&platform=0',
    ]

    def parse(self, response):
        item = exhibitionItem()
        coll_list = json.loads(response.text)["data"]["list"]
        for i in coll_list:
            exhibitionName = i["name"]
            exhibitionDescription = i["exhibitIntroduce"]
            exhibitionImageUrl = i["coverPic"]
            print((exhibitionName, exhibitionDescription, exhibitionImageUrl))
