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
    name = 'collection136'
    (1,2,1,1,2,1,1,1,2,1)
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.hzwhbwg.com/index.php/list-3.html']
    url='http://www.hzwhbwg.com/index.php/list-3-%d.html'
    page_num=2
    def parse(self, response):
        #scrapy crawl collection136
        item = collectionItem()
        a=('ys','gswhs')
        _list=response.xpath('//*[@class="product"]/ul/li')
        for li in _list:
            x=li.xpath('./a/img/@src').extract_first()
            coll_img='http://www.hzwhbwg.com'+x
            print(coll_img)
            coll_desc=''
            coll_name=''
        if self.page_num <= 5:
            new_url = (self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)