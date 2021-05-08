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
    name = 'collection159'
    (1,2,1,1,2,1,1,1,2,1)
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.slmmm.com/collection/8/1.html']
    url='https://www.slmmm.com/collection/8/%d.html'
    page_num=2
    cnt=1
    def parse(self, response):
        #scrapy crawl collection159
        item = collectionItem()
        _list=response.xpath('/html/body/div[2]/section/div/div[2]/div[1]/div/div')
        for li in  _list:
            coll_name=li.xpath('./div/div[2]/h3/text()').extract_first()
            print(coll_name)
            coll_img=li.xpath('./div/div[1]//@src').extract_first()
            print(coll_img)
            detail_url='https://www.slmmm.com'+li.xpath('./div/div[1]//@href').extract_first()
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
    
    def parse_detail(self,response):
        x=response.xpath('/html/body/div[2]/section/div/div//text()').extract()
        coll_desc=switch(x)
        print(coll_desc)