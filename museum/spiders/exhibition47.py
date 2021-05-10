import scrapy
from museum.items import exhibitionItem
import json


class Exhibition47Spider(scrapy.Spider):
    name = 'exhibition47'
    start_urls = [
        "http://www.gzsmzmuseum.cn/exhibi-1.html"
    ]

    def parse(self, response):
        item = exhibitionItem()
        title_list = response.xpath(
            "//ul[@class='newsli']//h3/a/text()").getall()
        description_list = response.xpath(
            "//ul[@class='newsli']//p/a/text()").getall()
        img_list = response.xpath(
            "//ul[@class='newsli']//img/@src").getall()
        for index, i in enumerate(img_list):
            exhibitionName = title_list[index]
            exhibitionDescription = description_list[index]
            exhibitionImageUrl = "http://www.gzsmzmuseum.cn/"+i
            print((exhibitionName, exhibitionImageUrl, exhibitionDescription))
            
