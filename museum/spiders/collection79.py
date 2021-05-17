import scrapy
from museum.items import collectionItem


class Collection79Spider(scrapy.Spider):
    name = 'collection79'
    start_urls = [
        "http://www.chinajiandu.cn/Collection/List/wj",
        "http://www.chinajiandu.cn/Collection/List/xhj",
        "http://www.chinajiandu.cn/Collection/List/yym"
    ]

    def parse_content(self, response):
        item = collectionItem()
        collectionImageUrl =response.urljoin(response.xpath("//div[@class='collectdetail clearfix ']//img/@src").get())
        collectionName = response.xpath(
            "//h1/text()").get()
        collectionDescription = "".join("".join(response.xpath(
            "//div[@class='cont']/p/text()").getall()).split())
        print((collectionName, collectionImageUrl,  collectionDescription))

    def parse(self, response):
        item_url = response.xpath("//ul[@class='collectlist ']//a/@href").getall()
        for i in item_url:
            yield scrapy.Request(response.urljoin(i),callback=self.parse_content)