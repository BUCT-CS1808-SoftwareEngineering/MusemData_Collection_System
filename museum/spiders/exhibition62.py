import scrapy
from museum.items import exhibitionItem

class Exhibition62Spider(scrapy.Spider):
    name = 'exhibition62'
    start_urls = [
        "https://www.cmnh.org.cn/list/?11_1.html"
    ]

    def parse(self, response):
        item = exhibitionItem()
        title_list = response.xpath(
            "//p[@class='pm']//a[@title]/@title").getall()
        description_list = response.xpath(
            "//p[@class='cp']/text()").getall()
        img_list = response.xpath(
            "//p[@class='pm']//img/@src").getall()
        for index, i in enumerate(img_list):
            exhibitionName = title_list[index]
            exhibitionDescription = "".join(description_list[index].split())
            exhibitionImageUrl = "https://www.cmnh.org.cn/"+i
            print((exhibitionName, exhibitionImageUrl, exhibitionDescription))
