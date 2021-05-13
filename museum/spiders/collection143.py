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
    name = 'collection143'
    (1,2,1,1,2,1,1,1,2,1)
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.teamuseum.cn/news/holding.htm']
    url='http://www.teamuseum.cn/news/holding.htm?newsType=%d'
    page_num=6
    def parse(self, response):
        #scrapy crawl collection143
        item = collectionItem()
        _list=response.xpath('//*[@id="waterfallProList"]//li')
        for li in _list:
            coll_name=li.xpath('.//h2/text()').extract_first()
            print(coll_name)
            detail_url=li.xpath('./a//@href').extract_first()
            detail_url='http://www.teamuseum.cn'+detail_url
            print(detail_url)
            coll_img=li.xpath('.//img/@src').extract_first()
            #coll_img='http://www.teamuseum.cn'+coll_img
            print(coll_img)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
    def parse_detail(self, response):
        item = response.meta["item"]
        x=response.xpath('//*[@class="pro_detail"]//text()').extract()
        coll_desc=''.join(x)
        #print(coll_desc)