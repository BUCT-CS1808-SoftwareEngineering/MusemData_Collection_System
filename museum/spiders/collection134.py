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
    name = 'collection134'
    (1,2,1,1,2,1,1,1,2,1)
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.ahgm.org.cn/ahgm/ahgm/gcjp/kw/index.html']
    url='http://www.ahgm.org.cn/ahgm/ahgm/gcjp/%s/index.html'
    page_num=2
    def parse(self, response):
        #scrapy crawl collection134
        item = collectionItem()
        a=('ys','gswhs')
        _list=response.xpath('//*[@class="gcjplist"]/li')
        for li in _list:
            x=li.xpath('./a/@href').extract_first()
            detail_url='http://www.ahgm.org.cn'+x
            print(detail_url)
            coll_img=li.xpath('.//img/@src').extract_first()
            coll_img='http://www.ahgm.org.cn'+coll_img
            print(coll_img)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        if self.page_num <= 3:
            new_url = (self.url%a[self.page_num-2])
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)
    def parse_detail(self,response):
        x=response.xpath('//*[@class="gcjp-infott"]/text()').extract_first()
        coll_name=x
        print(coll_name)
        coll_desc=''
