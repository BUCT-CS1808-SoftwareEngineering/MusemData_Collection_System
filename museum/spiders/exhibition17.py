import scrapy
from museum.items import exhibitionItem 
import re
import json
# scrapy crawl exhibition17

class Exhibition17Spider(scrapy.Spider):
    name = 'exhibition17'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.3gmuseum.cn/web/exhibitionHallOften/conventionalExhibitionPage.do?pageNumber=1&pageSize=12&itemno=25434353']

    # headers={
    #     'Host': 'www.3gmuseum.cn',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
    #     'Accept': 'application/json, text/javascript, */*; q=0.01',
    #     'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    #     'Accept-Encoding': 'gzip, deflate',
    #     'Referer': 'http://www.3gmuseum.cn/web/exhibitionHallOften/longExhibition.do?itemno=23&itemsonno=25434353',
    #     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    #     'X-Requested-With': 'XMLHttpRequest',
    #     'Content-Length': '40',
    #     'Origin': 'http://www.3gmuseum.cn',
    #     'Connection': 'keep-alive',
    #     'Cookie': 'JSESSIONID=16433817DCFCAFEF924469AD000E1054; UM_distinctid=1794b9a2a6354e-090ba774c3f989-4c3f2c72-1fa400-1794b9a2a6491a; CNZZDATA1254436347=90473301-1620471035-%7C1620471035',
    #     'Pragma': 'no-cache',
    #     'Cache-Control': 'no-cache'
    # }   headers=self.headers,

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse, method="POST")

    def parse(self, response):
        item = exhibitionItem()
        coll_list = json.loads(response.text)["list"]
        for i in coll_list:
            collectionName = i["formattitle"]
            collectionName = ''.join(collectionName)
            collectionImageUrl = i["themeimg"]
            collectionImageUrl = ''.join(collectionImageUrl)
            collectionDescription = str(i["contents"])
            collectionDescription = re.sub(r'<\/?.+?\/?>','',collectionDescription)
            # collectionDescription = ''.join(collectionDescription)
            # collectionImageUrl = 'http://www.njmuseum.com' + ''.join(collectionImageUrl)
            print((collectionName, collectionDescription, collectionImageUrl))
