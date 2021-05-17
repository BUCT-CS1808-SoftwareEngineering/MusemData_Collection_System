import scrapy
from museum.items import collectionItem


class Collection73Spider(scrapy.Spider):
    name = 'collection73'
    start_urls = [
        "http://www.sunyat-sen.org/index.php?m=content&c=index&a=lists&catid=173",
        "http://www.sunyat-sen.org/index.php?m=content&c=index&a=lists&catid=174",
        "http://www.sunyat-sen.org/index.php?m=content&c=index&a=lists&catid=175",
        "http://www.sunyat-sen.org/index.php?m=content&c=index&a=lists&catid=176",
        "http://www.sunyat-sen.org/index.php?m=content&c=index&a=lists&catid=177",
        "http://www.sunyat-sen.org/index.php?m=content&c=index&a=lists&catid=178"
    ]

    def parse_content(self, response):
        item = collectionItem()
        collectionImageUrl ="http://www.sunyat-sen.org"+response.xpath("//div[@class='zwpic']/img/@src").get()
        collectionName = response.xpath(
            "//h3/text()").get()
        collectionDescription = "".join("".join(response.xpath(
            "//div[@class='contentBox']//text()").getall()).split())
        print((collectionName, collectionImageUrl,  collectionDescription))

    def parse(self, response):
        item_url = response.xpath("//p[@class='ng_jsT']/a/@href").getall()
        for i in item_url:
            yield scrapy.Request(i,callback=self.parse_content)
        next_url = response.urljoin(response.xpath(
            "//div[@class='fY']/a[@class='a1']/@href").getall()[-1])
        if next_url != response.url:
            yield scrapy.Request(next_url)
