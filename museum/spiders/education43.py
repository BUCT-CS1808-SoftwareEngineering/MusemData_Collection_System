import scrapy
from museum.items import educationItem
import json


class Education43Spider(scrapy.Spider):
    name = 'education43'
    start_urls = [
        "http://www.beilin-museum.com/index.php?m=home&c=Lists&a=index&tid=96"
    ]

    def parse_content(self,response):
        educationName = response.xpath("//h1[1]/text()").get()
        educationDescription = "".join("".join(response.xpath('//div[@class="p"]/p/text()').getall()).split())
        
        educationImageUrl = response.xpath('//div[@class="p"]/p/img/@src').get()
        print((educationName,educationImageUrl,educationDescription))

    def parse(self, response):
        item = educationItem()
        item_list = response.xpath('//ul[@class="newslist"]/li/a/@href').getall()
        for index,i in enumerate(item_list):
            yield scrapy.Request("http://www.beilin-museum.com"+i,callback=self.parse_content)