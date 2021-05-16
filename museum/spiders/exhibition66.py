import scrapy
from museum.items import exhibitionItem

class Exhibition66Spider(scrapy.Spider):
    name = 'exhibition66'
    start_urls = [
        "http://www.gxmuseum.cn/a/exhibition/11/index.html"
    ]

    def parse(self, response):
        item = exhibitionItem()
        title_list = response.xpath(
            "//div[@class='listbox']/div/div[2]/p[1]/a/text()").getall()
        description_list = response.xpath(
            "//div[@class='listbox']/div/div[2]/p[3]/text()").getall()
        img_list = response.xpath(
            "//div[@class='listbox']/div//img/@src").getall()
        for index, i in enumerate(img_list):
            exhibitionName = title_list[index]
            exhibitionDescription = "".join(description_list[index*2+1].split())
            exhibitionImageUrl = "http://www.gxmuseum.cn"+i
            print((exhibitionName, exhibitionImageUrl, exhibitionDescription))
