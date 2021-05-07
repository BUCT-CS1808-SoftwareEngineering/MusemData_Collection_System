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
    name = 'collection142'
    (1,2,1,1,2,1,1,1,2,1)
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.chinasilkmuseum.com/zggd/list_21.aspx']
    url='https://www.chinasilkmuseum.com/zggd/list_21.aspx?page=%d'
    page_num=2
    cnt=1
    def parse(self, response):
        coll_name='南湖碑林'
        coll_img='http://www.nanhujng.com/images/images/main_bg.jpg'
        coll_desc=coll_name
        coll_name='珍贵藏品'
        coll_img='https://www.nanhujng.com/gcjp/zgcp/images/img_1.jpg'
        coll_desc=coll_name
        print(coll_img)