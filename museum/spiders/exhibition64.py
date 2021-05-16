import scrapy
from museum.items import exhibitionItem


class Exhibition64Spider(scrapy.Spider):
    name = 'exhibition64'
    start_urls = [
        "http://www.guilinmuseum.org.cn/Exhibition/Permanent/cszl"
    ]

    def parse_content(self, response):
        exhibitionName = response.meta['title'].split()[0]
        exhibitionDescription = "".join(response.xpath(
            "//div[@class='showcont']//p//text()").getall())
        exhibitionImageUrl = response.xpath(
            "//img/@src").get()
        print((exhibitionName, exhibitionImageUrl, exhibitionDescription))

    def parse(self, response):
        item = exhibitionItem()
        url_list = response.xpath(
            "//ul[@class='basiclist']//a/@href").getall()
        title_list = response.xpath("//h3[@class='ellipsis']//text()").getall()
        for index, url in enumerate(url_list):
            yield scrapy.Request(url.replace("Index.html", "qy.html"), callback=self.parse_content, meta={"title": title_list[index]})
