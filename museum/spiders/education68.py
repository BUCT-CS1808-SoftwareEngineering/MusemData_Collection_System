import scrapy
from museum.items import educationItem
import json


class Education68Spider(scrapy.Spider):
    name = 'education68'
    start_urls = [
        "http://www.zgshm.cn/kphd.html"
    ]

    def parse_content(self, response):
        item = educationItem()
        educationName = response.xpath(
            "//div[@class='news_conent_two_title']/text()").get()
        educationDescription = "".join("".join(response.xpath(
            "//p[@class='MsoNormal']//text()").getall()).split()).replace("\xa0", "")
        educationImageUrl = "http://www.gzsmzmuseum.cn/" + \
            response.xpath(
                "//p[@class='MsoNormal']/img/@src").get(default="images/main_logo.png")
        print((educationName, educationImageUrl, educationDescription))

    def parse(self, response):
        item_list = response.xpath(
            "//table//a/@href").getall()
        for index, i in enumerate(item_list):
            yield scrapy.Request("http://www.zgshm.cn"+i, callback=self.parse_content)
