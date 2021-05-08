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
    name = 'collection147'
    (1,2,1,1,2,1,1,1,2,1)
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.chinasilkmuseum.com/zggd/list_21.aspx']
    url='https://www.chinasilkmuseum.com/zggd/list_21.aspx?page=%d'
    page_num=2
    cnt=1
    def parse(self, response):
        coll_name='越窑青瓷'
        coll_img='http://www.nbmuseum.cn/images/121/yyqc_bg.jpg'
        coll_desc='http://www.nbmuseum.cn/col/col701/index.html'