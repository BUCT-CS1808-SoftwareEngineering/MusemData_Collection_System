import scrapy
from museum.items import educationItem


class Education73Spider(scrapy.Spider):
    name = 'education76'
    start_urls = [
        "http://www.gdmuseum.com/gdmuseum/_300858/_300870/index.html",
    ]

    def parse_content(self, response):
        item = educationItem()
        educationImageUrl = response.urljoin(response.xpath(
            "//div[@class='detail_cont']//img/@src").get())
        educationName = response.xpath(
            "//p[@class='title']/text()").get()
        educationDescription = "".join("".join(response.xpath(
            "//div[@class='detail_cont']//text()").getall()).split())
        print((educationName, educationImageUrl,  educationDescription))

    def parse(self, response):
        item_url = response.xpath("//div[@class='txt_cont']//a/@href").getall()
        for i in item_url:
            yield scrapy.Request(response.urljoin(i), callback=self.parse_content)
