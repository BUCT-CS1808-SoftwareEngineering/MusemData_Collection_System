import scrapy
from museum.items import collectionItem


class Collection45Spider(scrapy.Spider):
    name = 'collection45'
    url = "http://ynnmuseum.cn/collectionList/p/"

    def start_requests(self):
        for i in range(1,17):
            yield scrapy.Request(self.url+str(i),callback=self.parse)

    def parse_content(self, response):
        item = collectionItem()
        collectionImageUrl =response.xpath("//div[@class='img']/img/@src").get()
        collectionName = response.xpath(
            "//div[@class='c_boutique1']/div/div/div[@class='h40 syst']/text()").get()
        collectionDescription = "".join("".join(response.xpath(
            "//div[@class='h22']/text()").getall()).split())
        print((collectionName, collectionImageUrl,  collectionDescription))

    def parse(self, response):
        item_url = response.xpath("//div[@class='list']//a/@href").getall()
        for i in item_url:
            yield scrapy.Request(response.urljoin(i),callback=self.parse_content)
