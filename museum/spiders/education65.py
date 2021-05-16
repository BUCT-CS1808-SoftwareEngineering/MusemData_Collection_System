import scrapy
from museum.items import educationItem
import json


class Education65Spider(scrapy.Spider):
    name = 'education65'
    start_urls = [
        "http://www.amgx.org/more-16.html"
    ]

    def parse_content(self, response):
        educationName = response.xpath("//h4/text()").get()
        educationDescription = "".join("".join(response.xpath(
            "//td[@style='font-size:15px']/p/text()").getall()).split())
        educationImageUrl = "http://www.amgx.org" + \
            response.xpath(
                "//td[@style='font-size:15px']//img/@src").get("https://tva4.sinaimg.cn/crop.0.0.180.180.50/8903fbe3jw1e8qgp5bmzyj2050050aa8.jpg?KID=imgbed,tva&Expires=1621146034&ssig=ACAeJGMlv6")
        print((educationName, educationImageUrl, educationDescription))

    def parse(self, response):
        item = educationItem()
        item_list = response.xpath("//ul[@id='list']/li/a/@href").getall()
        for index, i in enumerate(item_list):
            yield scrapy.Request("http://www.amgx.org/"+i, callback=self.parse_content)
