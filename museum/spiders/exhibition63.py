import scrapy
from museum.items import exhibitionItem
import json


class Exhibition63Spider(scrapy.Spider):
    name = 'exhibition63'
    start_urls = [
        "http://www.hainanmuseum.org/hnbwgcms/node/162"
    ]

    def parse_content(self, response):
        exhibitionName = response.xpath(
            "//span[@class='f-left title']/text()").get()
        exhibitionDescription = "".join(response.xpath(
            "//div[@class='public-info-word']//p/span//text()").getall())
        exhibitionImageUrl = response.xpath(
            "//div[@class='public-info-word']//img/@src").get()
        print((exhibitionName, exhibitionImageUrl, exhibitionDescription))

    def parse(self, response):
        item = exhibitionItem()
        url_list = response.xpath(
            "//div[@onclick]/@onclick").getall()
        for index, i in enumerate(url_list):
            url = i.split("=")[1].replace("'","")
            yield scrapy.Request("http://www.hainanmuseum.org"+url, callback=self.parse_content)
