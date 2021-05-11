import scrapy
#scrapy crawl collection
#scrapy crawl exhiition
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
from museum.items import collectionItem
def switch(s):
        ss=''
        for i in s:
            ss+=str.strip(i)
            ss+='\n'
        return ss
def qutou(s):
    ss=''
    for i in s:
        if i=='：'or i=='，'or i==' 'or i=='。':break
        ss+=i
        
    return ss
class Collection124Spider(scrapy.Spider):
    name = 'collection160'
    (1,2,1,1,2,1,1,1,2,1)
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.shmmc.com.cn/Home/ZdzpList']
    url='https://www.slmmm.com/collection/8/%d.html'
    page_num=2
    cnt=1
    def parse(self, response):
        #scrapy crawl collection160
        item = collectionItem()
        _list=response.xpath('/html/body/div[2]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td/div/div/table/tbody/tr/td[2]/table/tbody/tr/td')
        for li in  _list:
            coll_name=li.xpath('.//text()').extract()
            coll_name=''.join(coll_name)
            coll_name=str.strip(coll_name)
            print(coll_name)
            coll_img=li.xpath('.//img/@src').extract_first()
            coll_img='https://www.shmmc.com.cn'+coll_img
            print(coll_img)
            detail_url='https://www.shmmc.com.cn'+li.xpath('.//a/@href').extract_first()
            coll_desc=detail_url
            print(detail_url)