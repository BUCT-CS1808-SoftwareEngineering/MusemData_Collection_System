import scrapy
from museum.items import collectionItem

class Collection87Spider(scrapy.Spider):
    name = 'collection87'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.ycbwg.com/web/explore/collection/list.shtml']

    url = 'http://www.ycbwg.com/web/explore/collection/list_%d.shtml'
    page_num = 2

    #详情页是动态加载  

    def parse(self, response):
        item = collectionItem()
        #/html/body/div/div[1]/div[3]/div/div[2]/div[3]/div[1]
        coll_list = response.xpath('/html/body/div/div[1]/div[3]/div/div[2]/div[3]/div[1]/ul/li')
        #//*[@id="thumbnailUL"]
        for li in coll_list:
            #/div[2]/a/h5/span[1]
            coll_name = li.xpath('./div[2]/a/h5/span[1]/text()').extract_first()
            print(coll_name)
            #/div[1]/a/img
            coll_img = li.xpath('./div[1]/a/img/@src').extract_first()
            
            coll_img = 'http://www.ycbwg.com' + coll_img
            print(coll_img)
            #yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        
        if self.page_num <= 5:
            new_url = (self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)
