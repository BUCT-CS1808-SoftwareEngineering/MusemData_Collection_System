import scrapy
from museum.items import exhibitionItem


class Exhibition75Spider(scrapy.Spider):
    name = 'exhibition75'
    start_urls = [
        "https://www.gznywmuseum.org/cswczs/index.jhtml"
    ]

    def parse(self, response):
        item = exhibitionItem()
        title_list = response.xpath(
            "//div[@class='wczc-fl-children-item']/p/text()").getall()
        img_list = response.xpath(
            "//div[@class='wczc-fl-children-item']/a/@href").getall()
        for index, i in enumerate(img_list):
            exhibitionName = title_list[index]
            exhibitionDescription = "无"
            exhibitionImageUrl = response.urljoin(i)
            print((exhibitionName, exhibitionImageUrl, exhibitionDescription))
