import scrapy
from museum.items import collectionItem
import json
#页面动态加载
class Collection110Spider(scrapy.Spider):
    name = 'collection110'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.jnmuseum.com/admin/pc/conllection/getListData.do?key=&museumId=&currentPage=1&size=1000&collectionType=TQ1&collectionYear=']

    def parse(self, response):
        item = collectionItem()
        coll_list = json.loads(response.text)["data"]
        for i in coll_list:
            coll_name = i["collectionName"]
            #coll_desc = i["mipOpenCulturalrelicInfo"]["collectionsCategory"]
            coll_img = i["picUrl"]
            print(coll_name)
            print(coll_img)
            #print(coll_desc)
