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
    name = 'exhibition141'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.zsbwg.com/myidea10/api/list/jibenchenglie-1-3']
    def parse(self, response):
        item = exhibitionItem ()
        #scrapy crawl exhibition141
        div_list = json.loads(response.text)["page"]["list"]
        for li in div_list:
            name = li["title"]
            print(name)
            y=li["zhengwen"]
            cont=switch1(y)
            cont=switch2(cont)
            print(cont)
            l=y.find("src")
            l+=5
            y=y[l:len(y)]
            r=y.find("style")
            img=y[0:r]
            img='https://www.zsbwg.com'+img
            print(img)