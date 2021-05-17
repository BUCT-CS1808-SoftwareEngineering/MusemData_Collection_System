import scrapy
from museum.items import collectionItem


class Collection69Spider(scrapy.Spider):
    name = 'collection69'
    start_urls = [
        "https://www.msrmuseum.com/News/Index/52",
        "https://www.msrmuseum.com/News/Index/53",
        "https://www.msrmuseum.com/News/Index/54",
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

    def parse_content(self,response):
        item = collectionItem()
        collectionName = response.xpath("//h1/text()").get()
        collectionDescription = "".join("".join(response.xpath("//div[@class='yf-detail']//text()").getall()).split())
        collectionImageUrl = response.urljoin(response.xpath("//div[@class='yf-detail']//img/@src").get())
        print((collectionName,collectionImageUrl,collectionDescription))

    def parse(self, response):
        item_list = response.xpath("//div[@class='yf-content']//a/@href").getall()
        for index,i in enumerate(item_list):
            yield scrapy.Request(response.urljoin(i), headers=self.headers,callback=self.parse_content)
        
