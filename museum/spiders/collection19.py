import scrapy
from selenium import webdriver
from museum.items import educationItem
import json
# scrapy crawl collection19
class Collection19Spider(scrapy.Spider):
    name = 'collection19'
    # allowed_domains = ['www.xxx.com']j
    start_urls = ['http://www.shanximuseum.com/sx/collection/collection_list?offset=0&count=327&dynasty=&material=&keyword=&categoryId=&quality=&_=1620530743320']

    def parse(self, response):
        item = educationItem()
        coll_list = json.loads(response.text)["data"]["list"]
        for i in coll_list:
            collectionName = i["title"]
            collectionName = ''.join(collectionName)
            collectionImageUrl = i["big_image"]
            collectionImageUrl = "http://www.shanximuseum.com" + ''.join(collectionImageUrl)
            detail_url = i["fullurl"]
            detail_url = ''.join(detail_url)
            print(detail_url)
            # collectionDescription = "\n文物类型：" + str(i["type"]) + "\n文物级别：" + str(i["level"]) + "\n完残程度：" + str(i["residuegrade"]) + "\n具体尺寸(cm)：" + str(i["size"])
            # collectionDescription = ''.join(collectionDescription)
            # collectionImageUrl = 'http://www.njmuseum.com' + ''.join(collectionImageUrl)
            print((collectionName, collectionImageUrl))

            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
    
    def parse_detail(self, response):
        item = response.meta["item"]
        # url = response.meta["url"]
        cont = response.xpath('/html/body/div[6]/div[4]/div/div[2]/div[1]//text()').extract()
        cont = ''.join(cont)
        time = "None"
        # if response.xpath('/html/body/div[6]/div[4]/div/div[1]/div[2]/text()').extract_first():
        time = response.xpath('/html/body/div[6]/div[4]/div/div[1]/div[2]/text()').extract_first()
        # print()
        cont = cont + "时代：" + time
        # cont = re.sub('&(.+?);','',cont)
        print(cont)
       
        # yield item
