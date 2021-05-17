import scrapy
from museum.items import exhibitionItem


class Exhibition79Spider(scrapy.Spider):
    name = 'exhibition79'
    start_urls = [
        "http://www.chinajiandu.cn/Exhibition/Index",
    ]

    def parse_content(self, response):
        item = exhibitionItem()
        exhibitionImageUrl = response.urljoin(response.xpath(
            "//div[@class='cont']//img/@src").get())
        exhibitionName = response.xpath(
            "//h1/text()").get().split()[0]
        exhibitionDescription = "".join("".join(response.xpath(
            "//div[@class='cont']//text()").getall()).split())
        print((exhibitionName, exhibitionImageUrl,  exhibitionDescription))

    def parse(self, response):
        item_url = response.xpath(
            "//ul[@class='exhibitionlist']//li/a/@href").getall()
        for i in item_url:
            yield scrapy.Request(response.urljoin(i), callback=self.parse_content)
