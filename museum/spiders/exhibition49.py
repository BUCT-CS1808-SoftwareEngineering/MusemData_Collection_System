import scrapy
from museum.items import exhibitionItem
import json
import re 
  


class Exhibition49Spider(scrapy.Spider):
    name = 'exhibition49'
    start_urls = [
        "http://www.zunyihy.cn/five_story.html"
    ]

    def parse(self, response):
        item = exhibitionItem()
        title_list = response.xpath(
            "//div[@class='txt']/div[1]/text()").getall()
        description_list = response.xpath(
            "//div[@class='txt']/div[2]/div/text()").getall()
        img_list = response.xpath(
            "//div[@class='tc_stroy']/div[1]/style/text()").getall()
        for index, i in enumerate(img_list):
            exhibitionName = title_list[index]
            exhibitionDescription = description_list[index]
            exhibitionImageUrl = "http://www.gzsmzmuseum.cn/"+self.find_url(i)
            print((exhibitionName, exhibitionImageUrl, exhibitionDescription))
            
    def find_url(self,string): 
        # findall() 查找匹配正则表达式的字符串
        url = re.findall('(?<=\()\S+(?=\))', string)[0]
        return url 