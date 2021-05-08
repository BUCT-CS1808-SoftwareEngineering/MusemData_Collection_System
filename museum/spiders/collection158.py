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
    name = 'collection158'
    (1,2,1,1,2,1,1,1,2,1)
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.yzmuseum.com/website/treasure/list.php']
    url='https://www.yzmuseum.com/website/treasure/list.php?page=%d&type=1'
    page_num=2
    cnt=1
    def parse(self, response):
        #scrapy crawl collection158
        item = collectionItem()
        _list=response.xpath('//*[@id="content_body"]/div')
        for li in  _list:
            coll_name=li.xpath('./a/span/div/p/text()').extract_first()
            #coll_name=str.strip(coll_name)
            print(coll_name)
            detail_url='https://www.yzmuseum.com/'+li.xpath('./a/@href').extract_first()
            print(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        if self.page_num <= 7:
            new_url = (self.url%(self.page_num))
            print(new_url)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)
        
    def parse_detail(self,response):
        coll_img='https://www.yzmuseum.com/'+response.xpath('//*[@id="content_cover"]/@src').extract_first()
        #coll_desc=''.join(x)
        print(coll_img)
        coll_desc=response.xpath('//*[@id="content_text"]//text()').extract()
        coll_desc=''.join(coll_desc)
        print(coll_desc)