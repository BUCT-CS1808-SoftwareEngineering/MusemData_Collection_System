import scrapy
from museum.items import educationItem

class Education64Spider(scrapy.Spider):
    name = 'education64'
    start_urls = [
        "http://www.guilinmuseum.org.cn/News/List/sjhd"
    ]

    def parse(self, response):
        item = educationItem()
        title_list = response.xpath(
            "//li[@class='clearfix']//h3/text()").getall()
        description_list = response.xpath(
            "//li[@class='clearfix']//p/text()").getall()
        img_list = response.xpath(
            "//li[@class='clearfix']/i/img/@src").getall()
        for index, i in enumerate(img_list):
            educationName = title_list[index].split()[0]
            educationDescription = description_list[index*2]
            educationImageUrl = i
            print((educationName, educationImageUrl, educationDescription))
