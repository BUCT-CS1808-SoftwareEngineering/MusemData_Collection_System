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
    name = 'collection131'
    (1,2,1,1,2,1,1,1,2,1)
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.mtybwg.org.cn/cangpin/113-1.aspx']
    
    cnt=1
    def parse(self, response):
        #scrapy crawl collection1
        item = collectionItem()
        x=response.xpath('//*[@id="container"]/li')
        url1='http://www.mtybwg.org.cn/cangpin/112-1.aspx'
        url2='http://www.mtybwg.org.cn/cangpin/112-2.aspx'
        url3='http://www.mtybwg.org.cn/cangpin/111-1.aspx'
        url4='http://www.mtybwg.org.cn/cangpin/110-1.aspx'
        url5='http://www.mtybwg.org.cn/cangpin/109-1.aspx'
        url6='http://www.mtybwg.org.cn/cangpin/109-2.aspx'
        url7='http://www.mtybwg.org.cn/cangpin/108-1.aspx'
        url8='http://www.mtybwg.org.cn/cangpin/107-1.aspx'
        url9='http://www.mtybwg.org.cn/cangpin/106-1.aspx'
        url10='http://www.mtybwg.org.cn/cangpin/286-1.aspx'
        url11='http://www.mtybwg.org.cn/cangpin/286-2.aspx'
        url12='http://www.mtybwg.org.cn/cangpin/282-1.aspx'
        urlll=('1',url1,url2,url3,url4,url5,url6,url7,url8,url9,url10,url11,url12)
        for li in x:
            y=li.xpath('./a[2]/text()').extract_first()
            coll_name=y
            print(y)
            y=li.xpath('./a[1]/@href').extract_first()
            detail_url='http://www.mtybwg.org.cn'+y
            #print(detail_url)
            y=li.xpath('./a[1]/img/@src').extract_first()
            coll_img='http://www.mtybwg.org.cn'+y
            print(coll_img)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        if self.cnt<=12:
            new_url=urlll[self.cnt]
            print(new_url)
            yield scrapy.Request(new_url,callback=self.parse)
            self.cnt+=1
    def parse_detail(self,response):
        coll_desc=response.xpath('/html/body/div[2]/div[2]/ul/div[3]/ul/text()').extract_first()
        print(coll_desc)
        