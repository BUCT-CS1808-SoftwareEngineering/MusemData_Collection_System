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
    name = 'collection154'
    (1,2,1,1,2,1,1,1,2,1)
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.wxmuseum.com/Collection/BookList/shbk']
    url='http://www.wxmuseum.com/Collection/BookList/shbk?page=%d'
    page_num=2
    cnt=1
    def parse(self, response):
        #scrapy crawl collection154
        item = collectionItem()
        _list=response.xpath('/html/body/div[5]/div/div/div/div[2]/ul[2]/li')
        for li in  _list:
            coll_name=li.xpath('.//h3/text()').extract_first()
            coll_name=str.strip(coll_name)
            coll_img=li.xpath('.//img/@src').extract_first()
            print(coll_img)
            print(coll_name)
            detail_url='http://www.wxmuseum.com'+li.xpath('./a/@href').extract_first()
            print(detail_url)
            coll_desc=coll_name
        if self.page_num <= 6:
            new_url = (self.url%(self.page_num))
            print(new_url)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)
            