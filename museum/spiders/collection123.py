import scrapy
#scrapy crawl collection
from museum.items import collectionItem
def switch(s):
        ss=''
        for i in s:
            ss+=i
            ss+="\n"
        return ss
class Collection123Spider(scrapy.Spider):
    name = 'collection123'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.aymuseum.com/nd.jsp?id=766#_jcp=4_2']
    url='http://www.aymuseum.com/nd.jsp?id=7%d#_jcp=4_2'
    page_num = 2
    def parse(self, response):
        item = collectionItem()
        coll_name = response.xpath('//*[@class="title"]//text()').extract_first()
        print(coll_name)
        y = response.xpath('//*[@class="richContent  richContent0"]//p/span/text()').extract()
        coll_desc=switch(y)
        print(coll_desc)
        coll_img=response.xpath('//*[@class="richContent  richContent0"]//img/@src').extract_first()
        print(coll_img)

        if self.page_num <= 5:
            new_url = (self.url%(self.page_num+65))
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)