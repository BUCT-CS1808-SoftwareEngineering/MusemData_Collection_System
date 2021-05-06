import scrapy
#scrapy crawl collection
#scrapy crawl exhiition
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
from museum.items import collectionItem
def switch(s):
        ss=''
        for i in s:
            ss+=i
            ss+="\n"
        return ss
def qutou(s):
    ss=''
    for i in s:
        if i=='：'or i=='，'or i==' 'or i=='。':break
        ss+=i
        
    return ss
class Collection124Spider(scrapy.Spider):
    name = 'collection138'
    (1,2,1,1,2,1,1,1,2,1)
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.ahm.cn/News/Details/cpzm?nid=11293']
    url='https://www.ahm.cn/News/Details/cpzm?nid=%d'
    page_num=2
    def parse(self, response):
        #scrapy crawl collection138
        item = collectionItem()
        a=(11252,11250,11213,11212,11180,11179,11202,11184,11169,11167,11166,11165,11071)
        _list=response.xpath('//table/tbody/tr')
        for li in _list:
            if len(li.xpath('./td[1]/text()').extract_first())==2:
                continue
            x=li.xpath('.//img/@src').extract_first()
            if x:
                coll_img='https://www.ahm.cn'+x
            else:coll_img=''
            coll_name=li.xpath('./td[2]/text()').extract_first()
            coll_desc=''
            print(coll_img)
            print(coll_name)
        if self.page_num <= 14:
            new_url = (self.url%a[self.page_num-2])
            print(new_url)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)
                