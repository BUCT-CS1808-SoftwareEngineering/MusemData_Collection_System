import scrapy
from museum.items import collectionItem
import json


class Collection53Spider(scrapy.Spider):
    name = 'collection53'
    start_urls = [
        "http://www.zgshm.cn/content.jsp?id=297e0fc278b0bdb20178f26f104b000a",
        "http://www.zgshm.cn/content.jsp?id=297e0fc2717d02b60171a4ebc22e0003",
        "http://www.zgshm.cn/content.jsp?id=297e0fc26e679f79017157b61e9b011e",
        "http://www.zgshm.cn/content.jsp?id=297e0fc26dce28e1016dd780cd10000b",
    ]

    def parse(self, response):
        item = collectionItem()
        collectionName = response.xpath(
            "//div[@class='news_conent_two_title']/text()").get()
        collectionDescription = "".join("".join(response.xpath(
            "//p[@class='MsoNormal']//text()").getall()).split()).replace("\xa0", "")
        collectionImageUrl = "http://www.gzsmzmuseum.cn/" + \
            response.xpath(
                "//p[@class='MsoNormal']/img/@src").get(default="images/main_logo.png")
        print((collectionName, collectionImageUrl, collectionDescription))
