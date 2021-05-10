import scrapy
from museum.items import educationItem
import json


class Education49Spider(scrapy.Spider):
    name = 'education49'
    start_urls = [
        "http://www.zunyihy.cn/training.html"
    ]

    def parse_content(self, response):
        educationName = response.xpath(
            "//div[@class='tit_com pd30']/div/text()").get()
        educationDescription = "".join(response.xpath(
            "//div[@class='situation_1']/p/text()").get().split())
        educationImageUrl = "http://www.gzsmzmuseum.cn/" + \
            response.xpath(
                "//div[@class='situation_1']/p/img/@src").get()
        print((educationName, educationImageUrl, educationDescription))

    def parse(self, response):
        item = educationItem()
        item_list = response.xpath(
            "//div[@class='train_5']//div[@class='li']//a/@href").getall()
        for index, i in enumerate(item_list):
            yield scrapy.Request("http://www.zunyihy.cn"+i, callback=self.parse_content)
