import scrapy
from museum.items import collectionItem


class Collection75Spider(scrapy.Spider):
    name = 'collection75'
    start_urls = [
        "https://www.gznywmuseum.org/yx/index.jhtml",
        "https://www.gznywmuseum.org/yq/index.jhtml",
        "https://www.gznywmuseum.org/tq/index.jhtml",
        "https://www.gznywmuseum.org/jyq/index.jhtml",
        "https://www.gznywmuseum.org/jtq/index.jhtml",
        "https://www.gznywmuseum.org/tqz/index.jhtml"
    ]

    def parse_content(self, response):
        item = collectionItem()
        collectionImageUrl = response.urljoin(
            response.xpath("//div[@class='zoompic']/img/@src").get())
        collectionDescription = "".join("".join(response.xpath(
            "//div[@class='cz-list-detail-view-info-content']//text()").getall()).split())
        collectionName = response.xpath(
            "//p[@class='cz-list-detail-view-info-title']/text()").get()
        print((collectionName, collectionImageUrl, collectionDescription))

    def parse_item(self, response):
        url_list = response.xpath(
            "//div[@class='cz-list-content']//a/@href ").getall()
        for i in url_list:
            yield scrapy.Request(response.urljoin(i), callback=self.parse_content)

    def parse(self, response):
        page_list = response.xpath(
            "//div[@class='page-large']//a/@onclick").getall()
        for i in page_list:
            url = response.urljoin(i.split("'")[1])
            yield scrapy.Request(url, callback=self.parse_item)
