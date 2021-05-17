import scrapy
from museum.items import collectionItem


class Collection107Spider(scrapy.Spider):
    name = 'collection107'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.ytmuseum.com/collection/cq?p=1']
    url = 'http://www.ytmuseum.com/collection/cq?p=%d'
    page_num = 2
    def parse_detail(self, response):
        item = response.meta["item"]
                          #/html/body/div[3]/div[3]/div[2]/div[2]/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/p/span[1]         
        if response.xpath('/html/body/div[3]/div[3]/div[2]/div[2]/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/p/span//text()'):
            coll_desc = response.xpath('/html/body/div[3]/div[3]/div[2]/div[2]/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/p/span//text()').extract()
            coll_desc = ''.join(coll_desc)
            print(coll_desc)  

    def parse(self, response):
        item = collectionItem()          
        coll_list = response.xpath('/html/body/div[2]/div[3]/div[2]/div[2]/ul/li')
       
        for div in coll_list:
            #/html/body/div[2]/div[3]/div[2]/div[2]/ul/li[1]/div[1]/span
            coll_name = div.xpath('./div[1]/span/text()').extract_first()
            print(coll_name)
            coll_img = 'http:'+ div.xpath('./div[2]/div[1]/a/img/@src').extract_first()
            #/html/body/div[2]/div[3]/div[2]/div[2]/ul/li[4]/div[2]/div[1]/a/img
            #http://services.ytta.cn
            print(coll_img)
            #/html/body/div[2]/div[3]/div[2]/div[2]/ul/li[1]/div[2]/div[1]/a
            detail_url = 'http://www.ytmuseum.com' + div.xpath('./div[2]/div[1]/a/@href').extract_first()
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})

        if self.page_num <= 8:
            new_url = (self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)