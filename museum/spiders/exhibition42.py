import scrapy
from museum.items import collectionItem
import json


class Exhibition42Spider(scrapy.Spider):
    name = 'exhibition42'
    start_urls = [
        'http://www.hylae.com/index.php?ac=article&at=list&tid=33',
        'http://www.hylae.com/index.php?ac=article&at=list&tid=34',
        'http://www.hylae.com/index.php?ac=article&at=list&tid=35',
    ]

    def parse(self, response):
        li_list = response.xpath("//div[@class='zhanlan-pic']//li/span[@class='xinxi']/a/@href").getall()
        for content_url in li_list:
            yield scrapy.Request(content_url, callback=self.content_parse)
        # 读取下一页
        next_page = response.xpath("//a[@title='»']/@href").get()
        if next_page != None:
            yield scrapy.Request(next_page, callback=self.parse)

    def content_parse(self, response):
        item = collectionItem()
        doc = response.xpath("//div[@class='zhanlan-pic']")
        collectionName = doc.xpath("./div[@class='list-right-bt']/text()").get()
        collectionImageUrl= "http://www.hylae.com" + doc.xpath(".//img/@src").get()
        collectionDescription = "".join("".join(doc.xpath(".//p//text()").getall()).split())#去除\xa0字符
        print((collectionName,collectionImageUrl,collectionDescription))