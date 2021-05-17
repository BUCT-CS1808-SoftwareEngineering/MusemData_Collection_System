import scrapy
from museum.items import exhibitionItem


class exhibition70Spider(scrapy.Spider):
    name = 'exhibition70'
    start_urls = [
        "https://www.gzam.com.cn/zzzc/list_18.aspx?State=0"
    ]

    def parse_content(self, response):
        item = exhibitionItem()
        exhibitionImageUrl = "https://www.gzam.com.cn"+response.meta["img"]
        exhibitionDescription = "".join("".join(response.xpath(
            "//div[@class='info_txt']//p//text()").getall()).split())
        exhibitionName = response.xpath("//h3/text()").get()
        print((exhibitionName, exhibitionImageUrl, exhibitionDescription))

    def parse(self, response):
        url_list = response.xpath(
            "//article[@class='SinglePage wsztBOX']//li/a/@href").getall()
        img_list = response.xpath(
            "//article[@class='SinglePage wsztBOX']//li/a/span/img/@src").getall()
        for index, i in enumerate(url_list):
            yield scrapy.Request("https://www.gzam.com.cn"+i, callback=self.parse_content, meta={"img": img_list[index]})
