import scrapy
from museum.items import collectionItem
import json


class Education42Spider(scrapy.Spider):
    name = 'education42'

    def start_requests(self):
        url = "http://www.hylae.com/index.php?ac=article&at=read&did="
        for i in range(100,111):
            yield scrapy.Request(url+str(i))

    def parse(self, response):
        item = collectionItem()
        doc = response.xpath("//div[@class='list-right']")
        educationName = doc.xpath(".//div[@class='list-right-bt']/text()").get()
        educationImageUrl= "http://www.hylae.com" + doc.xpath(".//img/@src").get(default="/upfile/2019/07/20190731171111_475.jpg")
        educationDescription = "".join("".join(doc.xpath(".//p//text()").getall()).split())#去除\xa0字符
        print((educationName,educationImageUrl,educationDescription))
