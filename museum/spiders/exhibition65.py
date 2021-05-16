import scrapy
from museum.items import exhibitionItem

class Exhibition65Spider(scrapy.Spider):
    name = 'exhibition65'
    start_urls = [
        "http://www.amgx.org/exhibimore-483.html"
    ]

    def parse(self, response):
        item = exhibitionItem()
        title_list = response.xpath(
            "//div[@class='mbright02t']/a/text()").getall()
        description_list = response.xpath(
            "//div[@class='lzhg']/table//p").getall()
        img_list = response.xpath(
            "//div[@class='lzhg']//img/@src").getall()
        for index, i in enumerate(img_list):
            exhibitionName = title_list[index]
            exhibitionDescription = "".join(description_list[index].split())
            exhibitionImageUrl = "http://www.amgx.org"+i
            print((exhibitionName, exhibitionImageUrl, exhibitionDescription))
