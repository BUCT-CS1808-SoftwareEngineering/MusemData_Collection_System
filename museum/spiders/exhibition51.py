import scrapy
from museum.items import exhibitionItem


class Exhibition51Spider(scrapy.Spider):
    name = 'exhibition51'
    start_urls = [
        "https://www.jc-museum.cn/display/"
    ]

    def parse_content(self, response):
        exhibitionName = response.xpath(
            "//div[@class='top_box wf100']/text()").get()
        exhibitionDescription = "".join(response.xpath(
            "//div[@class='lower_box wf100']/p//text()").get().split())
        exhibitionImageUrl = "http://www.gzsmzmuseum.cn/" + \
            response.xpath(
                "//div[@class='bd']//img/@src").get()
        print((exhibitionName, exhibitionImageUrl, exhibitionDescription))

    def parse(self, response):
        item = exhibitionItem()
        item_list = response.xpath(
            "//div[@class='list_box1 wf100']//a/@href").getall()
        for index, i in enumerate(item_list):
            yield scrapy.Request(response.urljoin(i), callback=self.parse_content)
