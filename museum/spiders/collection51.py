import scrapy
from museum.items import collectionItem
import time


class Collection51Spider(scrapy.Spider):
    name = 'collection51'
    start_urls = [
        "https://www.jc-museum.cn/display/list-7/list-17/page-1.html"
    ]

    def parse_content(self, response):
        item = collectionItem()
        collectionImageUrl = "https://www.jc-museum.cn" + \
            response.xpath("//div[@class='box2 wf100']/img/@src").get()
        collectionName = response.xpath(
            "//div[@class='box1 wf100']/span/text()").get()
        description = "".join("".join(response.xpath(
            "//div[@class='box2 wf100']//text()").getall()).split())
        print((collectionName, collectionImageUrl, description))

    def parse(self, response):
        next_page_symbol = response.xpath(
            "//div[@class='fanye wf100']/ul/li/a/text()").getall()[-1]
        if(next_page_symbol == "»"):
            next_page = response.xpath(
                "//div[@class='fanye wf100']/ul/li/a/@href").getall()[-1]
            time.sleep(0.2)
            yield scrapy.Request("https://www.jc-museum.cn"+next_page)
        url_list = response.xpath(
            "//div[@class='list_box3 wf100']//a/@href").getall()
        for i in url_list:
            time.sleep(0.2)
            yield scrapy.Request("https://www.jc-museum.cn"+i, callback=self.parse_content)
