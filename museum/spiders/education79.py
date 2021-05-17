import scrapy
from museum.items import educationItem


class Education79Spider(scrapy.Spider):
    name = 'education79'
    start_urls = [
        "http://www.chinajiandu.cn/News/List/xsjl"
    ]

    def parse_content(self, response):
        educationName = response.xpath("//h1/text()").get().split()[0]
        educationDescription = "".join("".join(response.xpath(
            "//div[@class='cont']/p/text()").getall()).split())
        educationImageUrl = response.xpath(
            "//div[@class='cont']//img/@src").get()
        print((educationName, educationImageUrl, educationDescription))

    def parse(self, response):
        item = educationItem()
        item_list = response.xpath(
            "//ul[@class='tempexhlist newslist']//a/@href").getall()
        for index, i in enumerate(item_list):
            yield scrapy.Request(response.urljoin(i), callback=self.parse_content)
