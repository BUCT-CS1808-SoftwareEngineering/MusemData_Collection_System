import scrapy
from museum.items import exhibitionItem 
import re
import json
# scrapy crawl education17

class Education17Spider(scrapy.Spider):
    name = 'education17'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.3gmuseum.cn/web/activity/findActivityArticleAndPage.do?itemno=34324333++++++++++++++++++++++++&pageNumber=1&pageSize=6&type=1']

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse, method="POST")

    def parse(self, response):
        item = exhibitionItem()
        coll_list = json.loads(response.text)["list"]
        for i in coll_list:
            collectionName = i["subject"]
            collectionName = ''.join(collectionName)
            collectionImageUrl = i["thumbnailimg"]
            # collectionImageUrl = ''.join(collectionImageUrl)
            collectionDescription = str(i["contents"])
            collectionDescription = re.sub(r'<\/?.+?\/?>','',collectionDescription)
            collectionDescription = re.sub('&(.+?);','',collectionDescription)
            if collectionName == '爷爷的那些事——“国强”展儿童观展手册':
                collectionDescription = collectionDescription + '：http://www.3gmuseum.cn/web_upfile/file/1571292824145013134.zip'
            # collectionDescription = ''.join(collectionDescription)
            # collectionImageUrl = 'http://www.njmuseum.com' + ''.join(collectionImageUrl)
            print((collectionName, collectionDescription, collectionImageUrl))
