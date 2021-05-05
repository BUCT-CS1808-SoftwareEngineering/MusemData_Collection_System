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
class Collection124Spider(scrapy.Spider):
    name = 'collection124'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.rjjng.com.cn/cangpin.thtml?id=10950']
    url2='http://www.rjjng.com.cn/cangpin.thtml?id=10951&&pn=%d'
    url3='http://www.rjjng.com.cn/cangpin.thtml?id=10952&&pn=%d'
    url4='http://www.rjjng.com.cn/cangpin.thtml?id=10953&&pn=%d'
    url5='http://www.rjjng.com.cn/cangpin.thtml?id=10954&&pn=%d'
    urll=(url2,url3,url4,url5)
    a={7,5,6,1,1}
    url='http://www.rjjng.com.cn/cangpin.thtml?id=10950&&pn=%d'
    page_num = 2
    cnt=0
    def parse(self, response):
        item = collectionItem()
        a=(7,5,6,1,1)
        div_list= response.xpath('/html/body/div[1]/div[3]/div/div[2]/ul//li')
        for li in div_list:
            coll_name=li.xpath('./a/h2/div[2]/text()').extract_first()
            print(coll_name)
            detail_url=li.xpath('./a/@href').extract_first()
            #print(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        if self.page_num <= a[self.cnt]:
            new_url = (self.url%self.page_num)
            self.page_num += 1
            #print(new_url)
            yield scrapy.Request(new_url,callback=self.parse)
        else :
            if self.cnt<=3:
                self.url =self.urll[self.cnt]
                self.page_num=1
                new_url = (self.url%self.page_num)
                self.page_num+=1
                self.cnt+=1
                #print(new_url)
                #print(self.cnt)
                yield scrapy.Request(new_url,callback=self.parse)
    def parse_detail(self,response):
        coll_desc=response.xpath('/html/body/div[1]/div[3]/div/div[2]/div/div[1]/p[2]/text()').extract_first()
        print(coll_desc)
        coll_img=response.xpath('/html/body/div[1]/div[3]/div/div[2]/div/div[1]/p[1]//img/@src').extract_first()
        print(coll_img)
        

