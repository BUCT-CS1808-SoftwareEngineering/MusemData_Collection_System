import scrapy
from museum.items import exhibitionItem


class Exhibition73Spider(scrapy.Spider):
    name = 'exhibition73'
    start_urls = [
        "http://www.sunyat-sen.org/index.php?m=content&c=index&a=lists&catid=10",
    ]

    def parse_content(self, response):
        item = exhibitionItem()
        exhibitionImageUrl = "http://www.sunyat-sen.org" + \
            response.xpath("//div[@class='conBox']//img/@src").get()
        exhibitionName = response.xpath(
            "//h3/text()").get()
        exhibitionDescription = "".join("".join(response.xpath(
            "//div[@class='contentBox']/p/text()").getall()).split())
        print((exhibitionName, exhibitionImageUrl,  exhibitionDescription))

    def parse(self, response):
        item_url = response.xpath("//p[@class='ng_jsT']/a/@href").getall()
        for i in item_url:
            yield scrapy.Request(i, callback=self.parse_content)
