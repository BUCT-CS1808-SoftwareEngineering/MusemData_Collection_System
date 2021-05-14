import scrapy
from museum.items import exhibitionItem


class Exhibition56Spider(scrapy.Spider):
    name = 'exhibition56'
    start_urls = [
        "http://www.zdm.cn/cooperation.html"
    ]

    def parse(self, response):
        item = exhibitionItem()
        title_list = response.xpath(
            "//div[@class='textBox col-lg-4']/a/p[1]/text()").getall()
        description_list = response.xpath(
            "//div[@class='textBox col-lg-4']/a/p[3]/text()").getall()
        img_list = response.xpath(
            "//div[@class='imgBox1 col-lg-8']/img/@src").getall()
        for index, i in enumerate(img_list):
            exhibitionName = "".join(title_list[index].split())
            exhibitionDescription = "".join(description_list[index].split())
            exhibitionImageUrl = i
            print((exhibitionName, exhibitionImageUrl, exhibitionDescription))
