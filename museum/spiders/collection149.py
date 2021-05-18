import scrapy
#scrapy crawl collection
#scrapy crawl exhiition
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
from museum.items import collectionItem
import json
def switch1(s):
    ss=''
    ff=0
    f1=0
    for i in s:
        if i=='<':
            ff=1
            continue
        if i=='>':
            ff=0
            continue
        if ff==0:
            ss+=i
        if  i=='。' or i==',':
            f1=1
    return ss
class Collection122Spider(scrapy.Spider):
    name = 'collection149'
    #allowed_domains = ['www.ccc.com']
    start_urls = ['http://www.zmnh.com/web?category=17&limit=100&dicType=1&keyWord=']
    page_num=2
    url='https://www.zsbwg.com/zhoushan1/man/antique?pageNumber=%d&pageSize=12&fengpinfeilei=8a7aef0958b37e280158b38d781e0033'
    def parse(self, response):
        item = collectionItem()
        #scrapy crawl collection149
        _list = json.loads(response.text)["data"]
        for li in _list:
            coll_name=li["title"]
            coll_img=li["img"]
            coll_img='http://www.zmnh.com/'+coll_img
            detail_url='http://www.zmnh.com/web/getInfo?limit=16&page=1&category=17&id=~'
            t=str(li["id"])
            detail_url=detail_url.replace('~',t)
            print(coll_name)
            print(coll_img)
            print(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
            #scrapy crawl collection149
    def parse_detail(self,response):
        x=json.loads(response.text)["content"]
        coll_desc=switch1(x)
        print(coll_desc)