import scrapy
#scrapy crawl collection129
from museum.items import collectionItem
def switch(s):
        ss=''
        for i in s:
            ss+=i
        return ss
class Collection123Spider(scrapy.Spider):
    name = 'collection129'
    #allowed_domains = ['www.xxx.com']
    cnt=0
    urll='http://www.gthyjng.com/gcww/wwjs/tdgmsq'
    
    start_urls = ['http://www.gthyjng.com/gcww/wwjs/tdgmsq/index_1.htm']
    def parse(self, response):
        item = collectionItem()
        self.cnt+=1
        if(self.cnt==5):
            self.urll='http://www.gthyjng.com/gcww/wwjs/krzzsq/'
        if(self.cnt==6):
            self.urll='http://www.gthyjng.com/gcww/wwjs/jfzzsq/'
        if(self.cnt==7):
            self.urll='http://www.gthyjng.com/gcww/wwjs/gjdww/'
        urlll=('1','1','http://www.gthyjng.com/gcww/wwjs/tdgmsq/index_2.htm','http://www.gthyjng.com/gcww/wwjs/tdgmsq','http://www.gthyjng.com/gcww/wwjs/tdgmsq/index_3.htm','http://www.gthyjng.com/gcww/wwjs/krzzsq/','http://www.gthyjng.com/gcww/wwjs/jfzzsq/','http://www.gthyjng.com/gcww/wwjs/jfzzsq/index_1.htm','http://www.gthyjng.com/gcww/wwjs/gjdww/')
        x=response.xpath('/html/body/div[4]/div/div[2]/div[2]/ul/li')
        for li in x:
            l1=li.xpath('.//img/@src').extract_first()
            l1=l1[1:len(l1)]
            coll_img=self.urll+l1
            print(coll_img)
            l1=li.xpath('./a/@href').extract_first()
            l1=l1[1:len(l1)]
            detail_url=self.urll+l1
            print(detail_url)
            print(self.cnt)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        if(self.cnt<=7):
            new_url=urlll[self.cnt+1]
            yield scrapy.Request(new_url,callback=self.parse)
    def parse_detail(self,response):
        x=response.xpath('/html/body/div[4]/div/div[2]/div[3]/div/div[2]//text()').extract()
        coll_desc=switch(x)
        print(coll_desc)
