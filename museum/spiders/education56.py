import scrapy
from museum.items import educationItem
import json


class Education56Spider(scrapy.Spider):
    name = 'education56'
    start_urls = [
        "http://www.zdm.cn/scenery.html"
    ]

    def parse_content(self, response):
        educationName = response.xpath(
            "//p[@class='title']/text()").get()
        educationDescription = "".join("".join(response.xpath(
            "//div[@class='textBox']/p/text()").getall()).split())
        educationImageUrl = response.xpath(
            "//div[@class='textBox']//img/@src").get()
        print((educationName, educationImageUrl, educationDescription))

    def parse(self, response):
        item = educationItem()
        item_list = response.xpath(
            "//div[@class='col-lg-7 textBox']/a/@href").getall()
        for i in item_list:
            yield scrapy.Request(i, callback=self.parse_content)
