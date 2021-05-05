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
    name = 'collection130'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.qzhjg.cn/html/jddc/20180131/681.html']
    url='http://www.qzhjg.cn/html/%s'
    cnt=0
    def parse(self, response):
        #scrapy crawl collection1
        item = collectionItem()
        a=('jddc/20180131/682.html','jddc/20131113/688.html','qzwxc/20140619/689.html','wyj/20160218/690.html')
        x=response.xpath('/html/body/div[1]/div[2]/div[5]/div[3]/div[2]/div[2]/ul/li')
        for li in x:
            coll_img='http://www.qzhjg.cn'+li.xpath('./a/img/@src').extract_first()
            print((coll_img))
            coll_desc=li.xpath('./a/img/@text').extract_first()
            print(coll_desc)
            coll_name=qutou(coll_desc)
            print(coll_name)
        if self.cnt<4:
            new_url = (self.url%a[self.cnt])
            print(new_url)
            self.cnt+=1
            yield scrapy.Request(new_url,callback=self.parse)