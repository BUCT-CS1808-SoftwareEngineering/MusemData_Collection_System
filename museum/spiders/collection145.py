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
    name = 'collection145'
    (1,2,1,1,2,1,1,1,2,1)
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.wzmuseum.cn/Col/Col5/Index_1.aspx']
    url='http://www.wzmuseum.cn/Col/Col5/Index_%d.aspx'
    page_num=2
    cnt=1
    def parse(self, response):
        #scrapy crawl collection145
        url1='http://www.wzmuseum.cn/Col/Col29/Index.aspx'
        url2='http://www.wzmuseum.cn/Col/Col30/Index.aspx'
        url3='http://www.wzmuseum.cn/Col/Col31/Index.aspx'
        url4='http://www.wzmuseum.cn/Col/Col32/Index.aspx'
        url5='http://www.wzmuseum.cn/Col/Col33/Index.aspx'
        url6='http://www.wzmuseum.cn/Col/Col34/Index.aspx'
        url7='http://www.wzmuseum.cn/Col/Col29/Index_2.aspx'
        urlll=('1',url1,url2,url3,url4,url5,url6,url7)
        item = collectionItem()
        a=(6,2,1,1)
        _list=response.xpath('/html/body/div[1]/div[4]/div[2]/div[2]/ul/li')
        for li in _list:
            coll_name=li.xpath('.//span/text()').extract_first()
            #detail_url='http://www.westlakemuseum.com'+li.xpath('./td/a/@href').extract_first()
            #coll_name=str.strip(coll_name)
            coll_img=li.xpath('./a/@href').extract_first()
            print(coll_name)
            print(coll_img)
            coll_desc=''
        if self.page_num <= 6:
            new_url = (self.url%self.page_num)
            print(new_url)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)
        else :
            if self.cnt<=7:
                new_url=urlll[self.cnt]
                print(new_url)
                self.cnt+=1
                yield scrapy.Request(new_url,callback=self.parse)
