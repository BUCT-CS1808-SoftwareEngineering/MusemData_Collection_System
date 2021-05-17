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
    s=s.replace('&hellip;','',1000)
    return s
class Education9Spider(scrapy.Spider):
    name = 'education144'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://47.98.149.60/hangbo/xuanjiao/list?catid=85&&pageNumber=&&pageSize=5']

    def parse(self, response):
        item = educationItem()
        #scrapy crawl education144
        div_list = json.loads(response.text)["detail"]["list"]
        for li in div_list:
            name = li["title"]
            print(name)
            detail_url='http://47.98.149.60/hangbo/search/lastPage?catid=85&id=~'
            t=str(li["id"])
            detail_url=detail_url.replace('~',t,2)
            print(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
            #scrapy crawl education144
    def parse_detail(self,response):
        x=json.loads(response.text)["detail"]
        for i in x:
            y=i["zhengwen"]
            cont=switch1(y)
            cont=switch2(cont)
            print(cont)
            l=y.find("src")
            l+=8
            r=y.find("style")
            img=y[l:r]
            img='http://47.98.149.60//'+img
            if len(img)>25:
                print(img)
            else:img=''
            break