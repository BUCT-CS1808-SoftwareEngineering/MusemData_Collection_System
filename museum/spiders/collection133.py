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
    name = 'collection133'
    (1,2,1,1,2,1,1,1,2,1)
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.ahbbmuseum.com/?list_4/']
    url='https://www.ahbbmuseum.com/?list_4_%d/'
    page_num=2
    def parse(self, response):
        #scrapy crawl collection133
        item = collectionItem()
        _list=response.xpath('//*[@id="lists"]//li')
        for div in _list:
            coll_name=div.xpath('.//img/@alt').extract_first()
            coll_img=div.xpath('.//img/@src').extract_first()
            coll_img='https://www.ahbbmuseum.com'+coll_img
            print(coll_name)
            print(coll_img)
            detail_url='https://www.ahbbmuseum.com'+div.xpath('.//a/@href').extract_first()
            print(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        if self.page_num <= 60:
            new_url = (self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)
    def parse_detail(self,response):
        x=response.xpath('//*[@class="content"]//p//text()').extract()
        ss=''
        for p in x:
            ss+=p
        print(ss)