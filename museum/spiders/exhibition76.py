import scrapy
from museum.items import exhibitionItem


class Exhibition76Spider(scrapy.Spider):
    name = 'exhibition76'
    start_urls = [
        "http://www.gdmuseum.com/gdmuseum/_300858/_300866/index.html",
    ]

    def parse_content(self, response):
        item = exhibitionItem()
        exhibitionImageUrl = response.urljoin(response.xpath(
            "//div[@class='detail_cont']//img/@src").get())
        exhibitionName = response.xpath(
            "//p[@class='title']/text()").get()
        exhibitionDescription = "".join("".join(response.xpath(
            "//div[@class='detail_cont']//text()").getall()).split())
        print((exhibitionName, exhibitionImageUrl,  exhibitionDescription))

    def parse(self, response):
        item_url = response.xpath("//div[@class='txt_cont']//a/@href").getall()
        for i in item_url:
            yield scrapy.Request(response.urljoin(i), callback=self.parse_content)
