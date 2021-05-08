import scrapy
from museum.items import exhibitionItem
import json
# import string
# scrapy crawl collection9


class Exhibition41Spider(scrapy.Spider):
    name = 'exhibition41'
    start_urls = [
        'https://www.xabwy.com/api/website/article/list?&currentPage=1&pageSize=1000&typeId=37',
        'https://www.xabwy.com/api/website/article/list?&currentPage=1&pageSize=1000&typeId=38',
        'https://www.xabwy.com/api/website/article/list?&currentPage=1&pageSize=1000&typeId=39',
        'https://www.xabwy.com/api/website/article/list?&currentPage=1&pageSize=1000&typeId=36',
        'https://www.xabwy.com/api/website/article/list?&currentPage=1&pageSize=1000&typeId=84',
    ]

    def parse(self, response):
        item = exhibitionItem()
        coll_list = json.loads(response.text)["body"]["list"]
        for i in coll_list:
            educationName = i["title"]
            educationDescription = i["description"]
            educationImageUrl = i["litPic"]
            print((educationName, educationDescription, educationImageUrl))
