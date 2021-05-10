import scrapy
from museum.items import collectionItem
import json


class Collection49Spider(scrapy.Spider):
    name = 'collection49'
    start_urls = [
        "http://www.zunyihy.cn/searchs/collection.html&tpl_file=collection&pagesize=40"
    ]

    def parse_content(self, response):
        collectionName = response.xpath("//div[@class='h_34']//text()").get()
        collectionDescription = "".join("".join(response.xpath(
            "//div[@class='situation_1']/p/text()").getall()).split())
        collectionImageUrl = "http://www.zunyihy.cn" + \
            response.xpath("//div[@class='bigimg']//img/@src").get(default= "/Uploads/Picture/2019/01/14/s5c3c48177d982.png")

        print((collectionName, collectionDescription, collectionImageUrl))

    def parse(self, response):
        item = collectionItem()
        url_list = response.xpath("//div[@id='datalist']//a/@href").getall()
        for i in url_list:
            yield scrapy.Request("http://www.zunyihy.cn"+i, callback=self.parse_content)
