import scrapy
from scrapy.http import headers
from museum.items import exhibitionItem


class Exhibition57Spider(scrapy.Spider):
    name = 'exhibition57'
    start_urls = [
        "http://www.cddfct.com/index.php"
    ]
    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        'Content-Length': '0',
        "Connection": "keep-alive"
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers=self.headers ,callback=self.parse)

    def parse_content(self, response):
        item = exhibitionItem()
        exhibitionImageUrl = response.xpath(
            "//div[@id='simTestContent']//img/@src").get()
        exhibitionName = response.xpath(
            "//div[@id='simTestContent']/h1/text()").get()
        exhibitionDescription = "".join("".join(response.xpath(
            "//div[@id='simTestContent']//span[@style='font-size: 9pt']/text()").getall()).split())
        print((exhibitionName, exhibitionImageUrl,  exhibitionDescription))

    def parse(self, response):
        url_list = response.xpath(
            "//ul[@class='carousel-list'][1]/li/a/@href").getall()
        for i in url_list:
            yield scrapy.Request("http://www.cddfct.com"+i,headers=self.headers, callback=self.parse_content)
