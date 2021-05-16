import scrapy
from museum.items import exhibitionItem


class Exhibition68Spider(scrapy.Spider):
    name = 'exhibition68'
    start_urls = [
        "http://www.ynmuseum.org/exhibition/display.html"
    ]

    def parse_content(self, response):
        exhibitionName = response.meta['title']
        exhibitionDescription = response.meta['description']
        exhibitionImageUrl = response.xpath(
            "//div[@class='content']//img/@src").get()
        print((exhibitionName, exhibitionImageUrl, exhibitionDescription))

    def parse(self, response):
        item = exhibitionItem()
        title_list = response.xpath(
            "//li[@class='arr_w']/div[@class='con']/div[@class='h3']/a/@title").getall()
        description_list = response.xpath(
            "//li[@class='arr_w']/div[@class='con']/div[@class='p']/text()").getall()
        url_list = response.xpath(
            "//li[@class='arr_w']/div[@class='con']/div[@class='h3']/a/@href").getall()
        for index, i in enumerate(url_list):
            yield scrapy.Request("http://www.ynmuseum.org"+i, callback=self.parse_content, meta={"title": title_list[index], "description": description_list[index]})
