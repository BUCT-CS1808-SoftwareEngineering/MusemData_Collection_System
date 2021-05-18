import scrapy
from museum.items import exhibitionItem 
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
    s=s.replace('&sect;','',1000)
    return s
class Education9Spider(scrapy.Spider):
    name = 'exhibition144'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://47.98.149.60/hangbo/zhanlan/list?catid=77&&pageNumber=&&pageSize=6']
    def parse(self, response):
        item = exhibitionItem ()
        #scrapy crawl exhibition144
        div_list = json.loads(response.text)["detail"]["list"]
        for li in div_list:
            name = li["title"]
            img=li["fengmian"]
            img='http://47.98.149.60//'+img
            detail_url='http://47.98.149.60/hangbo/zhanlan/detail?id=~'
            t=str(li["id"])
            detail_url=detail_url.replace('~',t,2)
            print(name)
            print(img)
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
           