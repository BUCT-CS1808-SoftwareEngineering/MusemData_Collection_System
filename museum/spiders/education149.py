import scrapy
from museum.items import educationItem
import json
#scrapy crawl collection
#scrapy crawl exhiition
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
#scrapy genspider education
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
def switch2(s):
    ss=''
    s=s.replace('&nbsp;','',1000)
    s=s.replace('&rdquo;','',1000)
    s=s.replace('&ldquo;','',1000)
    s=s.replace('&mdash;','',1000)
    s=s.replace('&hellip;','',1000)
    s=s.replace('&middot;','',1000)
    return s
class Education9Spider(scrapy.Spider):
    name = 'education149'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.zmnh.com/web/news/findRelationNews?entityId=11761&category=21&limit=5']

    def parse(self, response):
        item = educationItem()
        #scrapy crawl education149
        div_list = json.loads(response.text)["data"]
        for li in div_list:
            name = li["title"]
            name=switch2(name)
            print(name)
            img=li["img"]
            if img:
                img='http://www.zmnh.com/'+img
            print(img)
            detail_url='http://www.zmnh.com/web/getInfo?category=1&id=~'
            t=str(li["id"])
            detail_url=detail_url.replace('~',t,2)
            print(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
            #scrapy crawl education149
    def parse_detail(self,response):
            i=json.loads(response.text)["content"]
            y=i
            cont=switch1(y)
            cont=switch2(cont)
            print(cont)