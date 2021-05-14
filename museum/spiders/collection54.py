import scrapy
from museum.items import collectionItem


class Collection54Spider(scrapy.Spider):
    name = 'collection54'
    start_urls = [
        "http://www.sxd.cn/list_2.asp?bigclass=29"
    ]

    def parse_content(self, response):
        item = collectionItem()
        collectionImageUrl = "https://www.jc-museum.cn" + response.xpath("//div[@class='box2 wf100']/img/@src").get()
        collectionName = response.xpath(
            "//div[@class='box1 wf100']/span/text()").get()
        description = "".join(response.xpath(
            "//div[@class='box2 wf100']/p/span/text()").getall())
        if len(description) > 1:
            collectionDescription = "".join(description[1].split())
        else:
            collectionDescription = "无介绍"
        print((collectionName, collectionImageUrl, collectionDescription))

    def parse(self, response):
        page = str(response.body)
        print(page)