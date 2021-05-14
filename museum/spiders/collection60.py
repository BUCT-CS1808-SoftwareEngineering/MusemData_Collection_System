import scrapy
from museum.items import collectionItem


class Collection60Spider(scrapy.Spider):
    name = 'collection60'
    start_urls = [
        "http://www.dzshike.com/dazu//html/1//6/index.html"
    ]

    def parse(self, response):
        item = collectionItem()
        img_list = response.xpath(
            "//div[@class='imgdiv']//img/@src").getall()
        title_list = response.xpath(
            "//div[@class='fivemait']/div[1]/h2/text()").getall()
        description_list1 =response.xpath(
            "//div[@class='bei fr']/p[1]/text()").getall()
        description_list2 =response.xpath(
            "//div[@class='bei lf']/p[1]/text()").getall()
        for index, i in enumerate(img_list):
            collectionName = title_list[index]
            collectionDescription = description_list2[index // 2] if index % 2 == 0 else description_list1[index // 2]
            collectionImageUrl = i
            print((collectionName, collectionImageUrl,  collectionDescription))
        
