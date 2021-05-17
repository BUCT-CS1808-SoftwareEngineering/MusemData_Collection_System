import scrapy
from museum.items import collectionItem
import json


class Collection70Spider(scrapy.Spider):
    name = 'collection70'
    start_urls = [
        "https://www.gzam.com.cn/cp/list_24.aspx?lcid=3"
    ]

    def parse_content(self, response):
        item = collectionItem()
        collectionImageUrl = "http://www.ynmuseum.org" + \
            response.xpath(
                "//div[@class='yc_info']/img/@src").get()
        collectionDescription = "".join("".join(response.xpath(
            "//div[@class='yc_infoCon']/p//text()").getall()).split())
        collectionName = collectionDescription.split("》")[0]+"》"
        print((collectionName, collectionImageUrl, collectionDescription))

    def parse(self, response):
        url_list = response.xpath(
            "//dl[@class='dl']/dd/a/@href").getall()
        # title_list = response.xpath(
        #    "//p[@class='title']/text()").getall()
        for i in url_list:
            yield scrapy.Request("https://www.gzam.com.cn"+i, callback=self.parse_content)
        next_page = response.xpath(
            "//span[@class='p_page']/a/@href").getall()[-2]
        if next_page != "javascript:void(0);":
            yield scrapy.Request("https://www.gzam.com.cn"+next_page)
