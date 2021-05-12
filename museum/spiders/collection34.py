import scrapy
from selenium import webdriver
from museum.items import collectionItem
import json
# scrapy crawl collection34

class Collection34Spider(scrapy.Spider):
    name = 'collection34'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.qhmuseum.cn/qhm-webapi/api/v1/collection/getTextureAll?pageNumber=1&pageSize=100&texture=104',
    'http://www.qhmuseum.cn/qhm-webapi/api/v1/collection/getTextureAll?pageNumber=1&pageSize=12&texture=101',
    'http://www.qhmuseum.cn/qhm-webapi/api/v1/collection/getTextureAll?pageNumber=1&pageSize=22&texture=102',
    'http://www.qhmuseum.cn/qhm-webapi/api/v1/collection/getTextureAll?pageNumber=1&pageSize=10&texture=103',
    'http://www.qhmuseum.cn/qhm-webapi/api/v1/collection/getTextureAll?pageNumber=1&pageSize=10&texture=111',
    'http://www.qhmuseum.cn/qhm-webapi/api/v1/collection/getTextureAll?pageNumber=1&pageSize=10&texture=110',
    'http://www.qhmuseum.cn/qhm-webapi/api/v1/collection/getTextureAll?pageNumber=1&pageSize=10&texture=106',
    'http://www.qhmuseum.cn/qhm-webapi/api/v1/collection/getTextureAll?pageNumber=1&pageSize=10&texture=112']

    def parse(self, response):
        item = collectionItem()
        coll_list = json.loads(response.text)["data"]["list"]
        for i in coll_list:
            collectionName = i["collectionname"]
            collectionName = ''.join(collectionName)
            collectionImageUrl = i["collectionimages"]
            collectionImageUrl = ''.join(collectionImageUrl)
            collectionDescription = "\n时代：" + str(i["category"]) + "\n简介：" + str(i["collectiondescribe"])
            # collectionDescription = ''.join(collectionDescription)
            # collectionImageUrl = 'http://www.njmuseum.com' + ''.join(collectionImageUrl)
            print((collectionName,  collectionImageUrl))
            print(collectionDescription)