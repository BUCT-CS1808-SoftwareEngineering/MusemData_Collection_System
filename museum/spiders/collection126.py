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
    
class Collection124Spider(scrapy.Spider):
    name = 'collection126'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.81-china.com/collect/60.html']
    url2='http://www.81-china.com/collect/61/1.html'
    url3='http://www.81-china.com/collect/62/%d.html'
    url4='http://www.81-china.com/collect/117/%d.html'
    urll=(url2,url3,url4)
    url='http://www.81-china.com/collect/60/%d.html'
    page_num = 2
    cnt=0
    def parse(self, response):
        item = collectionItem()
        a=(18,1,5,1)
        div_list= response.xpath('/html/body/div[1]/div[5]/div[3]/div[2]/ul/li')
        for li in div_list:
            coll_name=li.xpath('./div[2]/h3/a/text()').extract_first()
            #print(coll_name)
            x=li.xpath('./div[2]/p//text()').extract()
            x=switch(x)
            #x=ge(x)
            #print(x)
            coll_desc=x
            print(len(x))
            if(len(x)>100):
                detail_url='http://www.81-china.com'+li.xpath('./div[2]/h3/a/@href').extract_first()
                print(detail_url)
                yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
            coll_img='http://www.81-china.com'+li.xpath('.//img/@src').extract_first()
            print(coll_name)
            #print(coll_desc)
            print(coll_img)
        if self.page_num <= 18:
            new_url = (self.url%(self.page_num))
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)
        else:
            
            yield scrapy.Request(self.url2,callback=self.parse2,meta={'item':item})
    def parse2(self,response):
        item = collectionItem()
        a=(18,1,5,1)
        div_list= response.xpath('/html/body/div[1]/div[5]/div[3]/div[2]/ul/li')
        for li in div_list:
            coll_name=li.xpath('./div[2]/h3/a/text()').extract_first()
            #print(coll_name)
            x=li.xpath('./div[2]/p//text()').extract()
            x=switch(x)
            #x=ge(x)
            #print(x)
            coll_desc=x
            if(len(x)>100):
                detail_url='http://www.81-china.com'+li.xpath('./div[2]/h3/a/@href').extract_first()
                print(detail_url)
                yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
            coll_img='http://www.81-china.com'+li.xpath('.//img/@src').extract_first()
            print(coll_name)
            #print(coll_desc)
            print(coll_img)

    def parse_detail(self,response):
        x=response.xpath('/html/body/div[1]/div[5]/div[4]//*[@class="detial_txt"]//text()').extract()
        
        x=switch(x)
        #x=ge(x)
        coll_desc=x
        print(coll_desc)

#scrapy crawl collection126