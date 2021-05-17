import scrapy
from museum.items import educationItem


class Education75Spider(scrapy.Spider):
    name = 'education75'
    start_urls = [
        "https://www.gznywmuseum.org/nygf/index.jhtml",
    ]

    def parse_content(self, response):
        item = educationItem()
        educationImageUrl = response.urljoin(response.xpath(
            "//div[@class='dsj-item-detail-content']//img/@src").get())
        educationName = response.xpath(
            "//p[@class='nbsp-sp-detail-title']/text()").get()
        educationDescription = "".join("".join(response.xpath(
            "//div[@class='dsj-item-detail-content']/p/span/text()").getall()).split())
        print((educationName, educationImageUrl,  educationDescription))

    def parse(self, response):
        item_url = response.xpath(
            "//div[@class='wczc-fl-children-view']//a/@href").getall()
        for i in item_url:
            yield scrapy.Request(response.urljoin(i), callback=self.parse_content)
