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
    name = 'collection151'
    (1,2,1,1,2,1,1,1,2,1)
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.zj-museum.com.cn/zjbwg/zjbwg/zs/jpww/qtq/index.html']
    url='http://www.zj-museum.com.cn/zjbwg/zjbwg/zs/jpww/qtq/index_%d.html'
    page_num=2
    cnt=1
    def parse(self, response):
        #scrapy crawl collection151
        item = collectionItem()
        _list=response.xpath('/html/body/div[3]/div[2]/div[2]/ul/li')
        for li in  _list:
            coll_name=li.xpath('./div/text()').extract_first()
            coll_img='http://www.zj-museum.com.cn'+li.xpath('./a/img/@src').extract_first()
            detail_url='http://www.zj-museum.com.cn'+li.xpath('./a/@href').extract_first()
            print(coll_img)
            print(coll_name)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        if self.page_num <= 3:
            new_url = (self.url%(self.page_num-1))
            print(new_url)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)
    def parse_detail(self,response):
        x=response.xpath('//*[@class="qtx-detail"]//text()').extract()
        coll_desc=switch(x)
        print(coll_desc)
            