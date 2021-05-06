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
    name = 'collection139'
    (1,2,1,1,2,1,1,1,2,1)
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.westlakemuseum.com/index.php/gcjp/jpzs2']
    url='https://www.ahm.cn/News/Details/cpzm?nid=%d'
    page_num=2
    def parse(self, response):
        #scrapy crawl collection139
        item = collectionItem()
        a=(11252,11250,11213,11212,11180,11179,11202,11184,11169,11167,11166,11165,11071)
        _list=response.xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form/table/tbody/tr')
        for li in _list:
            coll_name=li.xpath('./td/a/text()').extract_first()
            detail_url='http://www.westlakemuseum.com'+li.xpath('./td/a/@href').extract_first()
            coll_name=str.strip(coll_name)
            #print(coll_img)
            print(coll_name)
            print(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
    def parse_detail(self,response):
        x=response.xpath('//*[@class="item-page"]//td/img/@src').extract_first()
        if x:
            coll_img='http://www.westlakemuseum.com'+x
        else: coll_img='http://www.westlakemuseum.com/images/images2020/gcjp-ql-01.jpg'
        #print(coll_img)
        x=response.xpath('//*[@class="item-page"]//p/text()').extract()
        coll_desc=switch(x)
        print(coll_desc)