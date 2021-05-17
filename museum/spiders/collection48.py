import scrapy
from museum.items import collectionItem
import re

class Collection48Spider(scrapy.Spider):
    name = 'collection48'
    start_urls = [
        "http://www.gzmuseum.com/dl/gzjx/lr/",
    ]

    def parse_content(self, response):
        item = collectionItem()
        collectionImageUrl = response.xpath("//div[@class='Look_Window boxKj']//img/@src").get()
        collectionDescription = "".join("".join(response.xpath("//div[@class='Zoom']//text()").getall()).split())
        collectionName = response.xpath("//div[@class='Content boxKj']/div[@class='title']/text()").get()
        print((collectionName, collectionImageUrl, collectionDescription))

    def parse_page(self, response):
        url_list = response.xpath(
            "//div[@class='list_show']//a/@alt").getall()
        for index, i in enumerate(url_list):
            yield scrapy.Request(i, callback=self.parse_content)

    def parse(self, response):
        page_list = response.xpath(
            "//tr[@class='mudd_list']//script").getall()
        for i in page_list[1:]:
            url=re.findall("""(?<=href="\.\.).*?(?=" title)""",i)[0]
            yield scrapy.Request("http://www.gzmuseum.com/dl/gzjx"+url, callback=self.parse_page)
