import scrapy
from museum.items import exhibitionItem


class Exhibition53Spider(scrapy.Spider):
    name = 'exhibition53'
    start_urls = [
        "http://www.zgshm.cn/imglist.jsp?id=78abd44f3517405da73197aa6e9b0ccb"
    ]

    def parse(self, response):
        item = exhibitionItem()
        title_list = response.xpath(
            "//ul[@class='imglist']/li//label/text()").getall()
        description_list = response.xpath(
            "//ul[@class='imglist']/li//p/text()").getall()
        img_list = response.xpath(
            "//ul[@class='imglist']/li//img/@src").getall()
        for index, i in enumerate(img_list):
            exhibitionName = "".join(title_list[index].split())
            exhibitionDescription = "".join(description_list[index].split())
            exhibitionImageUrl = "http://www.zgshm.cn"+i
            print((exhibitionName, exhibitionImageUrl, exhibitionDescription))
