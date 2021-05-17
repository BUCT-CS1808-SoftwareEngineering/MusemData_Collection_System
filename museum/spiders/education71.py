import scrapy
from museum.items import educationItem
import json


class education71Spider(scrapy.Spider):
    name = 'education71'
    url = 'https://www.gzchenjiaci.com/MYwebsite/rc/Queryactivity'

    def start_requests(self):
        form_data = {'page': '1',
                     'limit': '40',
                     'activitytype': '0',
                     'articletype': '1'}
        yield scrapy.FormRequest(self.url, callback=self.parse, formdata=form_data)

    def parse(self, response):
        item = educationItem()
        coll_list = json.loads(response.text)["data"]
        for i in coll_list:
            educationName = i["title"]
            educationDescription = i["abstracts"]
            educationImageUrl = "https://www.gzchenjiaci.com"+i["imgurl"]
            print((educationName, educationDescription, educationImageUrl))
