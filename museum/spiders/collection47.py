import scrapy
from museum.items import collectionItem
import json

#一万多件藏品，慎爬
class Collection47Spider(scrapy.Spider):
    name = 'collection47'

    def start_requests(self):
        url = "http://www.gzsmzmuseum.cn/collection_search.html?page="
        for i in range(1,675):
            yield scrapy.Request(url+str(i))

    def parse(self, response):
        url_list = response.xpath("//table[@class='mzwx']//td/a/@href").getall()
        for i in url_list:
            yield scrapy.Request("http://www.gzsmzmuseum.cn/"+i,callback=self.parse_content)

    def parse_content(self, response):
        collectionName = response.xpath("//h3/text()").get()
        collectionDescription = "".join(response.xpath("//table//tr[1]/td/text()").getall())
        collectionImageUrl = response.xpath("//div[@class='right80p']/p/img/@src").get()
        print((collectionName, collectionDescription, collectionImageUrl))