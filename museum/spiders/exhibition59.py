import scrapy
from museum.items import exhibitionItem


class Exhibition59Spider(scrapy.Spider):
    name = 'exhibition59'
    start_urls = [
        "http://www.scmuseum.cn/list-1655.html"
    ]

    def parse(self, response):
        item = exhibitionItem()
        title_list = response.xpath(
            "//div[@class='zhanlan-article']/h5/text()").getall()
        description_list1 = response.xpath(
            "//div[@class='zhanlan-article']/p[1]/text()").getall()
        description_list2 = response.xpath(
            "//div[@class='zhanlan-article']/p[2]/text()").getall()
        img_list = response.xpath(
            "//div[@class='zhanlan-article']/img/@src").getall()
        for index, i in enumerate(img_list):
            exhibitionName = "".join(title_list[index].split())
            exhibitionDescription = description_list1[index]+description_list2[index]
            exhibitionImageUrl = i
            print((exhibitionName, exhibitionImageUrl, exhibitionDescription))
