import scrapy
from museum.items import educationItem


class Education45Spider(scrapy.Spider):
    name = 'education45'
    start_urls = [
        "http://ynnmuseum.cn/social_education.html"
    ]

    def parse_content(self, response):
        educationImageUrl = response.urljoin(response.xpath(
            "//div[@class='article']//img/@src").get())
        educationName = response.xpath(
            "//div[@class='h24']/text()").get()
        educationDescription = "".join("".join(response.xpath(
            "//div[@class='article-cont']//text()").getall()).split())
        print((educationName, educationImageUrl,  educationDescription))

    def parse(self, response):
        item = educationItem()
        item_list = response.xpath(
            "//div[@class='li scaleimg']//a/@href").getall()
        for index, i in enumerate(item_list):
            yield scrapy.Request(response.urljoin(i), callback=self.parse_content)
