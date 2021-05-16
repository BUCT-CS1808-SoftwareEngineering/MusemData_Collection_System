import scrapy
from museum.items import educationItem

class Education61Spider(scrapy.Spider):
    name = 'education61'
    start_urls = [
        "http://www.cqsxymjng.cn/channels/17.html"
    ]

    def parse(self, response):
        item = educationItem()
        title_list = response.xpath(
            "//span[@class='ct']//a/text()").getall()
        img_list = response.xpath(
            "//li[@class='clearfix']//img/@src").getall()
        for index, i in enumerate(img_list):
            educationName = title_list[index]
            educationDescription = "无介绍"
            educationImageUrl = i
            print((educationName, educationImageUrl, educationDescription))
