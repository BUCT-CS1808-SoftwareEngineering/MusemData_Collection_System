import scrapy
from museum.items import educationItem
import json
from lxml import etree

class Education80Spider(scrapy.Spider):
    name = 'education80'
    start_urls = [
        "http://api.shaoqiguli.com/api/CMS/getNewsList?channelno=baseres&pagesize=40&pageindex=1",
    ]


    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
        'Accept': 'application/json, text/plain, */*',
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        'Content-Length': '0',
        "Connection": "keep-alive",
        "Origin":"http://www.shaoqiguli.com",
        "Referer":"http://www.shaoqiguli.com/"
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers=self.headers ,callback=self.parse)

    def parse(self, response):
        item = educationItem()
        coll_list = json.loads(response.text)["data"]
        for i in coll_list:
            educationName = i["Title"]
            contentHTML =  i["Contents"]
            Selector = etree.HTML(contentHTML)
            educationDescription = "".join(Selector.xpath("//p/text()"))
            img_list = Selector.xpath("//img/@src")
            if (img_list!=[]):
                educationImageUrl = img_list[0]
            else:
                educationImageUrl = "无图片"
            print((educationName, educationDescription, educationImageUrl))
