import scrapy
from museum.items import educationItem
import json

class Education90Spider(scrapy.Spider):
    name = 'education90'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.hbww.org/ashx/ajax.ashx?type=Activity&year=&page=1&PageSize=1000&fldSort=StartTime&Sort=1&rnd=0.7001958616818901']   
                  
    def parse(self, response):
        item = educationItem()
        coll_list = json.loads(response.text)["Rows"]
        for i in coll_list:
            coll_name = i["Name"]
            coll_desc = i["Describe"]
            #coll_img = i[""]
            print(coll_name)
            print(coll_desc)
