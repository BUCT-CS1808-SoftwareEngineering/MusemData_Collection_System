import scrapy
from museum.items import educationItem

class Education70Spider(scrapy.Spider):
    name = 'education70'
    start_urls = [
        "https://www.gzam.com.cn/cn/list_92.aspx"
    ]

    def parse(self, response):
        item = educationItem()
        title_list = response.xpath(
            "///h4/a/text()").getall()
        description_list = response.xpath(
            "//li[@class='top']/p/text()").getall()
        img_list = response.xpath(
            "//li[@class='top']/a/img/@src").getall()
        for index, i in enumerate(img_list):
            educationName = title_list[index].split()[0]
            educationDescription = "".join(description_list[index].split())
            educationImageUrl = "https://www.gzam.com.cn"+i
            print((educationName, educationImageUrl, educationDescription))
