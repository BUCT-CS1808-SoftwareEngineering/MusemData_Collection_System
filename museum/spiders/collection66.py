import scrapy
from museum.items import collectionItem


class Collection66Spider(scrapy.Spider):
    name = 'collection66'
    start_urls = [
        "http://www.gxmuseum.cn/a/antique/16/index.html",
        "http://www.gxmuseum.cn/a/antique/17/index.html",
        "http://www.gxmuseum.cn/a/antique/18/index.html",
        "http://www.gxmuseum.cn/a/antique/19/index.html",
        "http://www.gxmuseum.cn/a/antique/20/index.html"
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
        collectionName = response.xpath("//h2/text()").get()
        collectionDescription = "".join("".join(response.xpath('//div[@class="neirong"]/p/text()').getall()).split())
        collectionImageUrl = "http://www.gxmuseum.cn"+response.xpath('//div[@class="neirong"]//img/@src').get()
        print((collectionName,collectionImageUrl,collectionDescription))

    def parse(self, response):
        item_list = response.xpath("//ul[@class='d5 mt2']//a/@href").getall()
        for index,i in enumerate(item_list):
            yield scrapy.Request("http://www.gxmuseum.cn"+i, headers=self.headers,callback=self.parse_content)
        next_page=response.xpath('//ul[@class="pagelist"]//a/@href').getall()[-2]
        next_page_name=response.xpath('//ul[@class="pagelist"]//a/text()').getall()[-2]
        if next_page_name=="下一页":
            yield scrapy.Request(response.urljoin(next_page), headers=self.headers,callback=self.parse)
        
