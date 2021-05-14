import scrapy
from museum.items import educationItem
import json


class Education47Spider(scrapy.Spider):
    name = 'education47'
    start_urls = [
        "http://www.gzsmzmuseum.cn/list-19.html"
    ]

    def parse_content(self, response):
        educationName = response.xpath("//h2/text()").get()
        educationDescription = "".join("".join(response.xpath(
            "//div[@class='detail_text']//span/text()").getall()).split())
        educationImageUrl = "http://www.gzsmzmuseum.cn/" + \
            response.xpath(
                "//div[@class='detail_text']//img/@src").get().replace('../../../', '')
        print((educationName, educationImageUrl, educationDescription))

    def parse(self, response):
        item = educationItem()
        item_list = response.xpath("//ul[@class='newsli']//a/@href").getall()
        for index, i in enumerate(item_list):
            yield scrapy.Request("http://www.gzsmzmuseum.cn/"+i, callback=self.parse_content)
