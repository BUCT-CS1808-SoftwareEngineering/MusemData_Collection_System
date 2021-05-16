import scrapy
from museum.items import collectionItem


class Collection65Spider(scrapy.Spider):
    name = 'collection65'
    start_urls = [
        "http://www.amgx.org/3dantiques.html"
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

    def parse(self,response):
        item = collectionItem()
        collectionNameList = response.xpath("//div[@class='videoli']//dd/a/text()").getall()
        collectionDescriptionList = response.xpath("//div[@class='videocover']/a/@title").getall()
        collectionImageUrlList = response.xpath("//div[@class='videocover']/a/img/@src").getall()
        for index,i in enumerate(collectionDescriptionList):
            collectionName = collectionNameList[index]
            collectionDescription = collectionDescriptionList[index] if collectionDescriptionList[index]!="" else "无介绍"
            collectionImageUrl = collectionImageUrlList[index]
            print((collectionName,collectionImageUrl,collectionDescription))

        
