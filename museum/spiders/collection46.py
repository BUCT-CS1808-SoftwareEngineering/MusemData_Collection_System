import scrapy
from museum.items import collectionItem
import json


class Collection46Spider(scrapy.Spider):
    name = 'collection46'
    start_urls = [
        "http://www.ynmuseum.org/appreciate/gem/bronze.html"
    ]

    def parse_content(self, response):
        collectionImageUrl = "http://www.ynmuseum.org" + \
            response.xpath(
                "//div[@class='prod_d_1']/div[@class='wrap']//img/@src").get()
        collectionName = response.xpath(
            "//div[@class='prod_d_1']/div[@class='wrap']//img/@alt").get()
        description = response.xpath(
            "//div[@class='prod_d_1']/div[@class='wrap']//div[@class='p']/text()").getall()
        if len(description) > 1:
            collectionDescription = "".join(description[1].split())
        else:
            collectionDescription = "无介绍"
        print((collectionName, collectionImageUrl, collectionDescription))

    def parse(self, response):
        item = collectionItem()
        url_list = response.xpath(
            "//ul[@class='prod_list cf']/li/a/@href").getall()
        for i in url_list:
            yield scrapy.Request("http://www.ynmuseum.org"+i, callback=self.parse_content)
        next_page = response.xpath(
            "//div[@class='page_w']/a[@class='next']/@href").get()
        if next_page != None:
            yield scrapy.Request("http://www.ynmuseum.org"+next_page)
