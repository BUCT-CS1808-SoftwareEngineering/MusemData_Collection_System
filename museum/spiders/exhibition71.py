import scrapy
from museum.items import exhibitionItem
import json
import re


class Exhibition71Spider(scrapy.Spider):
    name = 'exhibition71'
    start_urls = [
        'https://www.gzchenjiaci.com/MYwebsite/rc/findHGEHView?page=1&size=34',
    ]

    def parse(self, response):
        item = exhibitionItem()
        coll_list = json.loads(response.text)["data"]
        for i in coll_list:
            educationName = i["ehName"]
            educationDescription = re.sub('<[^<]+?>', '', i["ehContent"]).replace(
                '\n', '').strip().replace("&nbsp", "").replace(";", "")
            educationImageUrl = "https://www.gzchenjiaci.com"+i["ehImg"]
            print((educationName, educationDescription, educationImageUrl))
