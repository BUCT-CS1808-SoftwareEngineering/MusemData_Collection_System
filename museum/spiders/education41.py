import scrapy
from museum.items import educationItem
import json
# import string
# scrapy crawl collection9


class Education41Spider(scrapy.Spider):
    name = 'education41'
    start_urls = [
        'https://www.xabwy.com/api/website/article/list?&currentPage=1&pageSize=1000&typeId=51',
        'https://www.xabwy.com/api/website/article/list?&currentPage=1&pageSize=1000&typeId=52',
        'https://www.xabwy.com/api/website/article/list?&currentPage=1&pageSize=1000&typeId=53',
        'https://www.xabwy.com/api/website/article/list?&currentPage=1&pageSize=1000&typeId=54',
        'https://www.xabwy.com/api/website/article/list?&currentPage=1&pageSize=1000&typeId=55',
        'https://www.xabwy.com/api/website/article/list?&currentPage=1&pageSize=1000&typeId=56',

    ]

    def parse(self, response):
        item = educationItem()
        coll_list = json.loads(response.text)["body"]["list"]
        for i in coll_list:
            educationName = i["title"]
            educationDescription = i["description"]
            educationImageUrl = i["litPic"]
            print((educationName, educationDescription, educationImageUrl))
