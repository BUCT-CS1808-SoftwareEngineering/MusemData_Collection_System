import scrapy
from scrapy.http import headers
from museum.items import exhibitionItem


class Exhibition45Spider(scrapy.Spider):
    name = 'exhibition45'
    start_urls = [
        "http://ynnmuseum.cn/Exhibition_highlight.html"
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
            yield scrapy.Request(url, headers=self.headers, callback=self.parse)

    def parse_content(self, response):
        item = exhibitionItem()
        exhibitionImageUrl = response.urljoin(response.xpath(
            "//div[@class='article']//img/@src").get())
        exhibitionName = response.xpath(
            "//div[@class='h24']/text()").get()
        exhibitionDescription = "".join("".join(response.xpath(
            "//div[@class='article-cont']//text()").getall()).split())
        print((exhibitionName, exhibitionImageUrl,  exhibitionDescription))

    def parse(self, response):
        url_list = response.xpath(
            "//div[@class='li scaleimg']/div/a[1]/@href").getall()
        for i in url_list:
            yield scrapy.Request(response.urljoin(i), headers=self.headers, callback=self.parse_content)
