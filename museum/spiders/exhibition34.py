import scrapy
from museum.items import exhibitionItem 
import re
import json
# scrapy crawl exhibition34

class Exhibition34Spider(scrapy.Spider):
    name = 'exhibition34'
    start_urls = ['http://www.qhmuseum.cn/qhm-webapi/api/v1/exchange/exchangeFAll?pageNumber=1&pageSize=10&state=100']

    def parse(self, response):
        item = exhibitionItem()
        coll_list = json.loads(response.text)["data"]["list"]
        for i in coll_list:
            collectionName = i["title"]
            collectionName = ''.join(collectionName)
            collectionImageUrl = "http://www.qhmuseum.cn/static/img/nb.708d525.png"
            # collectionImageUrl = ''.join(collectionImageUrl)
            # detail_url = i["fullurl"]
            # detail_url = ''.join(detail_url)
            # print(detail_url)
            cont =  str(i["contents"])
            cont = re.sub(r'<(\n*)\/?.+?\/?(\n*)>','',cont)
            cont = re.sub('&(.+?);','',cont)
            # collectionDescription = ''.join(collectionDescription)
            # collectionImageUrl = 'http://www.njmuseum.com' + ''.join(collectionImageUrl)
            print((collectionName, collectionImageUrl))
            print(cont)
