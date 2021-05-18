import scrapy
from museum.items import exhibitionItem
import json

class Exhibition110Spider(scrapy.Spider):
    name = 'exhibition110'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.jnmuseum.com/admin/pc/esaleShow/getListData.do?type=1&museumId=&currentPage=1&size=9']

    def parse(self, response):
        item = exhibitionItem()
        coll_list = json.loads(response.text)["data"]
        for i in coll_list:
            coll_name = i["showName"]
            coll_desc = i["showDescription"]
            #coll_img = i[""]
            print(coll_name)
            print(coll_desc)

