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
        return ss
        #1
def switch1(s):
    ss=''
    ff=0
    f1=0
    for i in s:
        if i=='<':
            ff=1
            continue
        if i=='>':
            ff=0
            continue
        if ff==0:
            ss+=i
        if  i=='。' or i==',':
            f1=1
    return ss
def switch2(s):
    ss=''
    ff=0
    f1=0
    for i in s:
        if i=='<':
            ff=1
            continue
        if i=='>':
            ff=0
            continue
        if ff==0:
            ss+=i
        if  i=='。' or i==',':
            f1=1
    if f1==1:
        return ss
    return ''
def zhaotu(str):
    cnt=0
    l=0
    r=0
    for i in str:
        if(str[cnt:cnt+3]=="src"):
            l=cnt
        if(str[cnt]=='"'and cnt>l+4 and l!=0):
            r=cnt
        cnt+=1
    return 'http://www.jgsgmbwg.com/'+str[l+5:r]
class Collection124Spider(scrapy.Spider):
    name = 'collection125'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.jgsgmbwg.com/bwgnews.php?cid=71&page=1']
    url='http://www.jgsgmbwg.com/bwgnews.php?cid=71&page=%d'
    page_num = 5
    def parse(self, response):
        item = collectionItem()
        li_list=response.xpath('/html/body/div[1]/div[5]/div[2]/div/ul/li')
        cnt=0
        for li in li_list:
            detail_url='http://www.jgsgmbwg.com/'+li.xpath('span[3]/a/@href').extract_first()
            print(detail_url)
            cnt+=1
            if cnt==13:
                break
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
    def parse_detail(self,response):
        _list=response.xpath('//*[@id="textarea"]/*').extract()
        s=''
        ch=-1
        m=''
        for i in _list:
            j=switch2(i)
            s+=j
            if i[3]=='a':
                m=zhaotu(i)
            if(i[1]=='h'):
                ch+=1
                if ch!=0:
                    #print(s)
                    coll_desc=s
                    coll_img=m
                    print(coll_name)
                    print(coll_desc)
                    print(coll_img)  
                coll_name=switch1(i)
                s=''
        coll_desc=s
        coll_img=m
        print(coll_name)
        print(coll_desc)  
        print(coll_img)
                
                    
                
        

        #scrapy crawl collection125
        