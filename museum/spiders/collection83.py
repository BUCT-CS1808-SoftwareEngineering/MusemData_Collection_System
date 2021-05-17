import scrapy
from museum.items import collectionItem
import re

#动态加载
class Collection83Spider(scrapy.Spider):
    name = 'collection83'
    #allowed_domains = ['www.xxx.com']
    

    start_urls = ['http://www.zhongshanwarship.org.cn/wenwu.html']
    #http://61.187.53.122/list.aspx?id=8&lang=zh-CN&page=1
    #url = 'http://61.187.53.122/list.aspx?id=8&lang=zh-CN&page=%d'
    #page_num = 2

    def parse_detail(self, response):
        item = response.meta["item"]
        #//*[@id="divContent"]
        #/html/body/div[3]/div/div[2]/div/p[1]/span/span
        if response.xpath('/html/body/div[3]/div/div[2]/div/p[1]/span/span//text()'):
            coll_desc = response.xpath('/html/body/div[3]/div/div[2]/div/p[1]/span/span//text()').extract()
            coll_desc = ''.join(coll_desc)
            print(coll_desc)  

    def parse(self, response):
        item = collectionItem()
        #//*[@id="caseListDIV"]
        coll_list = response.xpath('//*[@id="caseListDIV"]/div')
        #//*[@id="thumbnailUL"]
        for div in coll_list:
            coll_name = div.xpath('./div/a/span/text()').extract_first()
            print(coll_name)
            detail_url = 'http://www.zhongshanwarship.org.cn/' + li.xpath('./div/a/@href').extract_first()
            coll_img = li.xpath('./div/a/img/@src').extract_first()
            #http://61.187.53.122/
            #coll_img = 'http://61.187.53.122' + coll_img
            print(coll_img)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        
        #if self.page_num <= 14:
            #new_url = (self.url%self.page_num)
            #self.page_num += 1
            #yield scrapy.Request(new_url,callback=self.parse)