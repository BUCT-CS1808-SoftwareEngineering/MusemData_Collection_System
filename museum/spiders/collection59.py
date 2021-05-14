
import scrapy
from museum.items import collectionItem


class Collection59Spider(scrapy.Spider):
    name = 'collection59'
    start_urls = [
        "http://www.scmuseum.cn/thread-366-117.html",
        "http://www.scmuseum.cn/thread-387-117.html",
        "http://www.scmuseum.cn/thread-348-117.html",
        "http://www.scmuseum.cn/thread-327-117.html",
        "http://www.scmuseum.cn/thread-311-117.html",
        "http://www.scmuseum.cn/thread-287-117.html",
        "http://www.scmuseum.cn/thread-265-117.html",
        "http://www.scmuseum.cn/thread-243-117.html",
        "http://www.scmuseum.cn/thread-224-117.html"
    ]

    def parse(self, response):
        item = collectionItem()
        collectionImageUrl = "http://www.scmuseum.cn"+response.xpath(
            "//div[@class='sgportfolio-img']/img/@src").get()
        collectionName = response.xpath(
            "//h1/text()").get()
        collectionDescription = "".join("".join(response.xpath(
            "//div[@id='MyContent']/p/text()").getall()).split())
        next_page = response.xpath(
            "//div[@class='sbp-content'][2]/p[1]/a/@href").get()
        if (next_page != None):
            yield scrapy.Request(next_page)
        print((collectionName, collectionImageUrl,  collectionDescription))
