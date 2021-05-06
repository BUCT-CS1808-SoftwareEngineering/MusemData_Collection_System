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
    name = 'collection148'
    (1,2,1,1,2,1,1,1,2,1)
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.chinasilkmuseum.com/zggd/list_21.aspx']
    url='https://www.chinasilkmuseum.com/zggd/list_21.aspx?page=%d'
    page_num=2
    cnt=1
    def parse(self, response):
        #scrapy crawl collection148
        item = collectionItem()
        a=(126,35,5,3)
        url1='https://www.chinasilkmuseum.com/zgxd/list_22.aspx?page=%d'
        url2='https://www.chinasilkmuseum.com/xf/list_23.aspx?page=%d'
        url3='https://www.chinasilkmuseum.com/mzx/list_24.aspx?page=%d'
        urlll=('1',url1,url2,url3)
        _list=response.xpath('/html/body/div[1]/div/div[8]/div/ul/li')
        for li in _list:
            coll_name=li.xpath('./p/a/text()').extract_first()
            #detail_url='http://www.westlakemuseum.com'+li.xpath('./td/a/@href').extract_first()
            coll_name=str.strip(coll_name)
            coll_img='https://www.chinasilkmuseum.com'+li.xpath('./a/img/@src').extract_first()
            print(coll_name)
            print(coll_img)
            detail_url='https://www.chinasilkmuseum.com'+li.xpath('./a/@href').extract_first()
            #print((detail_url))
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        if self.page_num <= a[self.cnt-1]:
            new_url = (self.url%self.page_num)
            print(new_url)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)
        else :
            if self.cnt<=3:
                self.url=urlll[self.cnt]
                self.cnt+=1
                new_url=(self.url%1)
                print(new_url)
                self.page_num=2
                yield scrapy.Request(new_url,callback=self.parse)
    def parse_detail(self,response):
        x=response.xpath('//*[@class="detail_text"]//text()').extract()
        coll_desc=switch(x)
        print(coll_desc)
        
        