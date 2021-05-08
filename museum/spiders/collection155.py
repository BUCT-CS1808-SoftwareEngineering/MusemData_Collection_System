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
    name = 'collection155'
    (1,2,1,1,2,1,1,1,2,1)
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.xzmuseum.com/collection_list.aspx?category_id=500']
    url='https://www.xzmuseum.com/collection_list.aspx?category_id=500&page=%d'
    page_num=2
    cnt=1
    def parse(self, response):
        #scrapy crawl collection155
        item = collectionItem()
        _list=response.xpath('/html/body/div[4]/div/div[2]/div[2]/div[2]/ul/li')
        for li in  _list:
            coll_name=li.xpath('./a/p/text()').extract_first()
            #coll_name=str.strip(coll_name)
            coll_img='https://www.xzmuseum.com/'+li.xpath('.//img/@src').extract_first()
            print(coll_img)
            print(coll_name)
            detail_url='https://www.xzmuseum.com/'+li.xpath('./a/@href').extract_first()
            print(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        if self.page_num <= 948:
            new_url = (self.url%(self.page_num))
            print(new_url)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)
    def parse_detail(self,response):
        x=response.xpath('/html/body/div[4]/div/div[2]/div[2]/div[2]/div[3]//text()').extract()
        coll_desc=''.join(x)
        print(coll_desc)