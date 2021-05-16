import scrapy
from museum.items import collectionItem
import json


class Collection62Spider(scrapy.Spider):
    name = 'collection62'
    start_urls = [
        "https://www.cmnh.org.cn/list/?26.html"
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
        collectionName = response.xpath("//h1[2]").get()
        collectionDescription = "".join("".join(response.xpath('//span[@style]/text()').getall()).split())
        collectionImageUrl = response.xpath('//div[@class="newsxx_nr"]//img/@src').get()
        print((collectionName,collectionImageUrl,collectionDescription))

    def parse(self, response):
        item_list = response.xpath("//p[@class='pm']/a/@href").getall()
        for index,i in enumerate(item_list):
            yield scrapy.Request("https://www.cmnh.org.cn"+i, headers=self.headers,callback=self.parse_content)
        next_page=response.xpath('//div[@class="page_nav"]/a/@href').getall()[-2]
        next_page_name=response.xpath('//div[@class="page_nav"]/a/text()').getall()[-2]
        if next_page_name=="下一页":
            yield scrapy.Request("https://www.cmnh.org.cn/list/"+next_page, headers=self.headers)
        
