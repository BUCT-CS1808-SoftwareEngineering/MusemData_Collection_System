import scrapy
from museum.items import collectionItem


class Collection56Spider(scrapy.Spider):
    name = 'collection56'
    start_urls = [
        "http://www.zdm.cn/treasure.html"
    ]

    def parse_content(self, response):
        item = collectionItem()
        collectionImageUrl = response.meta['img']
        collectionName = response.xpath(
            "//div[@class='titleBox']/p/text()").get()
        collectionDescription = "".join("".join(response.xpath(
            "//div[@class='textBox']//text()").getall()).split())
        print((collectionName, collectionImageUrl,  collectionDescription))

    def parse(self, response):
        url_list = response.xpath(
            "//div[@class='row listItemBox']//a/@href").getall()
        img_list = response.xpath(
            "//div[@class='row listItemBox']/div/a/div/img/@src").getall()
        for index, i in enumerate(url_list):
            yield scrapy.Request("http://www.zdm.cn"+i, callback=self.parse_content, meta={"img": img_list[index]})
