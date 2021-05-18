import scrapy
from museum.items import collectionItem
import json

class Collection90Spider(scrapy.Spider):
    name = 'collection99'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.wwsdw.net/mip/front/OCCollection/info.do?yearType=&collectionUnit=133&collectionsCategory=&order=2&key=&currentPage=1']
                  
    def parse(self, response):
        item = collectionItem()
        coll_list = json.loads(response.text)["data"]["mociList"]
        for i in coll_list:
            coll_name = i["mipOpenCulturalrelicInfo"]["name"]
            coll_desc = i["mipOpenCulturalrelicInfo"]["collectionsCategory"]
            coll_img = i["picture"]["url"]
            print(coll_name)
            print(coll_img)
            print(coll_desc)
            




