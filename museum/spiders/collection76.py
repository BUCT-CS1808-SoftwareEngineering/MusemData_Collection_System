import scrapy
from museum.items import collectionItem


class Collection76Spider(scrapy.Spider):
    name = 'collection76'
    start_urls = [
        "http://www.gdmuseum.com/gdmuseum/_300746/index.html",
    ]

    def parse_content(self, response):
        item = collectionItem()
        collectionImageUrl = response.meta['img']
        collectionDescription = "".join("".join(response.xpath(
            "//div[@class='cont']//text()").getall()).split())
        if collectionDescription == "":
            collectionDescription = "".join("".join(response.xpath(
                "//div[@class='cp_list']//span/@name").getall()).split())
        collectionName = response.xpath(
            "//div[@class='js_title show_title']/p/text()").get()
        print((collectionName, collectionImageUrl, collectionDescription))

    def parse_page(self, response):
        url_list = response.xpath(
            "//div[@class='js_img']/a[@class='pro_img']/@href").getall()
        img_list = response.xpath(
            "//a[@class='pro_img']/span/img/@src").getall()
        for index, i in enumerate(url_list):
            yield scrapy.Request(response.urljoin(i), callback=self.parse_content, meta={"img": response.urljoin(img_list[index])})

    def parse(self, response):
        page_list = response.xpath(
            "//div[@class='product_list']/div[@class='product']/a[@class='product_img']/@href").getall()
        for i in page_list:
            yield scrapy.Request(response.urljoin(i), callback=self.parse_page)
