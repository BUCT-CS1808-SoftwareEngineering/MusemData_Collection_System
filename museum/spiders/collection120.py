import scrapy
from museum.items import collectionItem

class Collection120Spider(scrapy.Spider):
    name = 'collection120'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.qingdaomuseum.com/collection/category/28']
    url = 'http://www.qingdaomuseum.com/collection/category/28/%d'
    page_num = 2
    def parse_detail(self, response):
        item = response.meta["item"]    
        if response.xpath('/html/body/div[6]/div[2]/div/div[4]/div/p//text()'):
            coll_desc = response.xpath('/html/body/div[6]/div[2]/div/div[4]/div/p//text()').extract()
            coll_desc = ''.join(coll_desc)
            print(coll_desc)  

    def parse(self, response):
        item = collectionItem()          
        coll_list = response.xpath('/html/body/div[6]/div[2]/div/div[2]/div')
        #/html/body/div[3]/div/div[2]/table[1]/tbody/tr/td/div/table/tbody/tr[1]/td[1]
        for div in coll_list:
            #/html/body/div[6]/div[2]/div/div[2]/div[1]/div/h5/b
            coll_name = div.xpath('./div/h5/b/text()').extract_first()
            print(coll_name)
            #/html/body/div[6]/div[2]/div/div[2]/div[1]/div/div/a
            coll_img =  div.xpath('./div/div/a/img/@src').extract_first()          
            print(coll_img)
           
            detail_url =  div.xpath('./div/div/a/@href').extract_first()
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        if self.page_num <= 3:
            new_url = (self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)

