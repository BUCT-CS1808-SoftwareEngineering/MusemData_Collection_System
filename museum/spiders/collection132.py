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
    name = 'collection132'
    (1,2,1,1,2,1,1,1,2,1)
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.fjbwy.com/node_124.html#nav']
    url='http://www.fjbwy.com/node_124_%d.html#nav'
    page_num=2
    def parse(self, response):
        #scrapy crawl collection132
        item = collectionItem()
        _list=response.xpath('//*[@class="zstuk"]')
        for li in _list:
            coll_name=li.xpath('.//@title').extract_first()
            coll_img=li.xpath('.//img/@src').extract_first()
            print(coll_name)
            print(coll_img)
            detail_url=li.xpath('.//a/@href').extract_first()
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        if self.page_num <= 19:
            new_url = (self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)
    def parse_detail(self,response):
        a=response.xpath('//*[@class="nr_smzw"]//p/text()').extract()
        coll_desc=switch(a)
        print(coll_desc)



