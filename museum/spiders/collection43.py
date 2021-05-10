import scrapy
from museum.items import collectionItem
import json


class Collection43Spider(scrapy.Spider):
    name = 'collection43'
    start_urls = [
        "http://www.beilin-museum.com/index.php?m=home&c=Lists&a=index&tid=74"
    ]

    def parse_content(self,response):
        collectionName = response.xpath("//h1[1]/text()").get()
        collectionDescription = "".join("".join(response.xpath('//div[@class="p"]/p/text()').getall()).split())
        collectionImageUrl = response.meta['image']
        print((collectionName,collectionImageUrl,collectionDescription))

    def parse(self, response):
        item = collectionItem()
        item_list = response.xpath('//ul[@class="imglist"]/li/a')
        urls = item_list.xpath("@href").getall()
        imgs = response.xpath('//ul[@class="imglist"]/li/a/img/@src').getall()
        for index,i in enumerate(urls):
            yield scrapy.Request("http://www.beilin-museum.com"+i,callback=self.parse_content,meta={"image":"http://www.beilin-museum.com"+imgs[index]})
        next_page=response.xpath("//ul[@class='pagination']/li/a/@href").getall()[-2]
        if next_page!=None:
            yield scrapy.Request("http://www.beilin-museum.com"+next_page)
        
