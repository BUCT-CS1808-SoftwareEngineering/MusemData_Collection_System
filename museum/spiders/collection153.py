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
    name = 'collection153'
    #allowed_domains = ['www.ccc.com']
    start_urls = ['http://www.csmuseum.cn/api/services/app/InfoService/GetArchivesInfoList2?SkipCount=0&MaxResultCount=1000&categoryId=6&status=1']
    page_num=2
    url='https://www.zsbwg.com/zhoushan1/man/antique?pageNumber=%d&pageSize=12&fengpinfeilei=8a7aef0958b37e280158b38d781e0033'
    def parse(self, response):
        item = collectionItem()
        #scrapy crawl collection153
        _list = json.loads(response.text)["result"]["data"]["items"]
        for li in _list:
            coll_name=li["title"]
            coll_img=li["imgUrl"]
            coll_img='http://www.csmuseum.cn/'+coll_img
            detail_url='http://www.csmuseum.cn/api/services/app/ArchivesService/GetArchivesInfoDetail?id=~'
            t=str(li["id"])
            detail_url=detail_url.replace('~',t)
            print(coll_name)
            print(coll_img)
            print(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
            #scrapy crawl collection153
    def parse_detail(self,response):
        x=json.loads(response.text)["result"]["data"]["content"]
        coll_desc=switch1(x)
        print(coll_desc)