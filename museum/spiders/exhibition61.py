import scrapy
from museum.items import exhibitionItem

class Exhibition61Spider(scrapy.Spider):
    name = 'exhibition61'
    start_urls = [
        "http://www.cqsxymjng.cn/channels/428.html"
    ]

    def parse(self, response):
        item = exhibitionItem()
        title_list = response.xpath(
            "//span[@class='ct']//a/text()").getall()
        description_list = response.xpath(
            "//li[@class='clearfix']//div/text()").getall()
        img_list = response.xpath(
            "//li[@class='clearfix']//img/@src").getall()
        print(description_list)
        for index, i in enumerate(img_list):
            exhibitionName = title_list[index]
            exhibitionDescription = description_list[index]
            exhibitionImageUrl = i
            print((exhibitionName, exhibitionImageUrl, exhibitionDescription))
