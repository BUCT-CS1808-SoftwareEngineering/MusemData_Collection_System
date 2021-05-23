import scrapy
from museum.items import collectionItem
import re
import json


class Collection58Spider(scrapy.Spider):
    name = 'collection58'
    start_urls = [
        "http://www.jinshasitemuseum.com/Treasure",
    ]
    url = "http://www.jinshasitemuseum.com/Treasure/Index?nodeName="
    new_urls = []
    deep_urls = []
    js1_urls = []
    js2_urls = []
    js3_urls = []

    def parse_content(self, response):
        item = collectionItem()
        collectionName = response.xpath(
            "//li[@data-pic]//img/@name1").get()
        collectionDescription = "".join("".join(response.xpath(
            "//li[@data-pic]//img/@name2").getall()).split())
        collectionImageUrl = response.xpath(
            "//li[@data-pic]//img/@src").get()
        collectionImageUrl = re.sub("\\\\","/",collectionImageUrl)
        print((collectionName, collectionImageUrl, collectionDescription))
        item['collectionName'] = collectionName
        item['museumID'] = 58
        item['collectionIntroduction'] = collectionDescription
        item['collectionImage'] = collectionImageUrl
        yield item

    def parse(self, response):
        page_list = response.xpath(
            "//div[@class='innerNav']/a/@onclick").getall()
        for i in page_list:
            yield scrapy.Request(self.url+i.split("'")[1],callback=self.parse_content)
