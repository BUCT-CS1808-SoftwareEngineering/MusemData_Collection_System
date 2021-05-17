import scrapy
from museum.items import exhibitionItem


class Exhibition69Spider(scrapy.Spider):
    name = 'exhibition69'
    start_urls = [
        "https://www.msrmuseum.com/News/Index/27"
    ]

    def parse_content(self, response):
        exhibitionName = response.meta['title']
        exhibitionImageUrl = response.meta['img']
        exhibitionDescription = response.xpath(
            "//div[@class='yf-detail']//text()").get().split()[0]
        print((exhibitionName, exhibitionImageUrl, exhibitionDescription))

    def parse(self, response):
        item = exhibitionItem()
        title_list = response.xpath(
            '//ul[@class="list-inline yf-media-list yf-mgl0"]/li/a/strong/text()').getall()
        img_list = response.xpath(
            '//ul[@class="list-inline yf-media-list yf-mgl0"]/li/a/span/img/@src').getall()
        url_list = response.xpath(
            '//ul[@class="list-inline yf-media-list yf-mgl0"]/li/a/@href').getall()

        for index, i in enumerate(url_list):
            yield scrapy.Request("https://www.msrmuseum.com"+i, callback=self.parse_content, meta={"title": title_list[index], "img": img_list[index]})
