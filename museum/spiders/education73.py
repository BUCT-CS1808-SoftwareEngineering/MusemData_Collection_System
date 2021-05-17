import scrapy
from museum.items import educationItem


class Education73Spider(scrapy.Spider):
    name = 'education73'
    start_urls = [
        "http://www.sunyat-sen.org/index.php?m=content&c=index&a=lists&catid=75",
    ]

    def parse_content(self, response):
        item = educationItem()
        educationImageUrl = "http://www.sunyat-sen.org" + \
            response.xpath("//div[@class='conBox']//img/@src").get()
        educationName = response.xpath(
            "//h3/text()").get()
        educationDescription = "".join("".join(response.xpath(
            "//div[@class='contentBox']/p/text()").getall()).split())
        print((educationName, educationImageUrl,  educationDescription))

    def parse(self, response):
        item_url = response.xpath("//ul[@class='conli']/li//a/@href").getall()
        for i in item_url:
            yield scrapy.Request("http://www.sunyat-sen.org/"+i, callback=self.parse_content)
