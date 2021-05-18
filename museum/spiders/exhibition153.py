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
    name = 'exhibition153'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.csmuseum.cn/api/services/app/EventsService/GetEventsList?SkipCount=0&MaxResultCount=6&status=99&typeId=10&orderType=20&saleId=']
    def parse(self, response):
        item = exhibitionItem ()
        #scrapy crawl exhibition153
        div_list = json.loads(response.text)["result"]["data"]["items"]
        for li in div_list:
            name = li["eventName"]
            img=li["imgUrl"]
            img='http://www.csmuseum.cn'+img
            print(name)
            print(img)
            cont=li["eventContent"]
            cont=switch1(cont)
            cont=switch2(cont)
            print(cont)