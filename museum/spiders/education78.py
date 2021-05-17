import scrapy
from museum.items import educationItem
import json


class Education78Spider(scrapy.Spider):
    name = 'education78'
    start_urls = [
        'https://www.csm.hn.cn/cbeducate/actInfo/getActInfoList.shtml?pageIndex=1&pageSize=10&noCatch=1621261457000',
    ]

    def parse(self, response):
        item = educationItem()
        coll_list = json.loads(response.text)["data"]["recordsList"]
        for i in coll_list:
            educationName = i["vTitle"]
            educationDescription = i["contentSummary"]
            educationImageUrl = i["imgUrl"]
            print((educationName, educationDescription, educationImageUrl))
