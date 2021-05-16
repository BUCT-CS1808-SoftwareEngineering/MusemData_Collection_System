import scrapy
from museum.items import educationItem


class Education66Spider(scrapy.Spider):
    name = 'education66'
    start_urls = [
        "http://www.gxmuseum.cn/a/education/23/index.html"
    ]

    def parse_content(self, response):
        educationName = response.xpath("//h2/text()").get()
        educationDescription = "".join("".join(response.xpath(
            "//td[@id='contentText']/p[1]/text()").getall()).split())
        educationImageUrl = "无图片"
        print((educationName, educationImageUrl, educationDescription))

    def parse(self, response):
        item = educationItem()
        item_list = response.xpath("//ul[@class='d1']//li//a/@href").getall()
        for index, i in enumerate(item_list):
            yield scrapy.Request("http://www.gxmuseum.cn"+i, callback=self.parse_content)
