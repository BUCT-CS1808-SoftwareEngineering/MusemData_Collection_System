import scrapy
from museum.items import exhibitionItem
import json


class Exhibition43Spider(scrapy.Spider):
    name = 'exhibition43'
    start_urls = [
        "http://www.beilin-museum.com/index.php?m=home&c=Lists&a=index&tid=72"
    ]

    def parse_content(self,response):
        exhibitionName = response.xpath("//h1[1]/text()").get()
        exhibitionDescription = "".join("".join(response.xpath('//div[@class="p"]/p/text()').getall()).split())
        exhibitionImageUrl = response.xpath('//div[@class="p"]/p/img/@src').get()
        print((exhibitionName,exhibitionImageUrl,exhibitionDescription))

    def parse(self, response):
        item = exhibitionItem()
        item_list = response.xpath('//ul[@class="piclist"]/li/a/@href').getall()
        for index,i in enumerate(item_list):
            yield scrapy.Request("http://www.beilin-museum.com"+i,callback=self.parse_content)