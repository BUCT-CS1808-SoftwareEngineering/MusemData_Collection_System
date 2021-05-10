import scrapy
from museum.items import educationItem
import json


class Education46Spider(scrapy.Spider):
    name = 'education46'
    start_urls = [
        "http://www.ynmuseum.org/education/events.html"
    ]

    def parse(self, response):
        item = educationItem()
        title_list = response.xpath(
            "//div[@class='video_list cf']//img/@title").getall()
        description_list = response.xpath(
            "//div[@class='video_list cf']//img/@alt").getall()
        img_list = response.xpath(
            "//div[@class='video_list cf']//img/@src").getall()
        for index, i in enumerate(title_list):
            educationName = title_list[index]
            educationDescription = description_list[index]
            educationImageUrl = img_list[index]
            print((educationName, educationImageUrl, educationDescription))