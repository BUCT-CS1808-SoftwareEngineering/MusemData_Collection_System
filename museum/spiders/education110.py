import scrapy
from museum.items import educationItem
import json

class Education90Spider(scrapy.Spider):
    name = 'education110'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.jnmuseum.com/admin/pc/activity/getActivityListByType.do?type=&size=100&currentPage=1']   
                  
    def parse(self, response):
        item = educationItem()
        coll_list = json.loads(response.text)["data"]
        for i in coll_list:
            coll_name = i["activityName"]
            #coll_desc = i[""]
            coll_img = i["picUrl"]
            print(coll_name)
            print(coll_img)


