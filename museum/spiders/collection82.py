import scrapy
from museum.items import collectionItem

class Collection82Spider(scrapy.Spider):
    name = 'collection82'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.changjiangcp.com/list/158.html?page=1']
    url = 'http://www.changjiangcp.com/list/158.html?page=%d'
    page_num = 2
    
    #详情页“检查”和“网页源码”无反应
    def parse_detail(self, response):
        item = response.meta["item"]
        
        #coll_img = response.xpath('/html/body/div[6]/div/div[1]/div[1]/div[1]/div/div/a/@src').extract_first()
        #coll_img = 'http://www.changjiangcp.com' + coll_img
        #print(coll_img)
       
      
        if response.xpath('/html/body/div[6]/div/div[1]/div[2]/div[2]/p[1]/text()'):
         
            coll_desc = response.xpath('/html/body/div[6]/div/div[1]/div[2]/div[2]/p[1]/text()').extract_first()
            #coll_desc = ''.join(coll_desc)
            print(coll_desc)
        

    def parse(self, response):
        item = collectionItem()
        #//*[@id="gallery-wrapper"]
        coll_list = response.xpath('//*[@id="gallery-wrapper"]/div')
        #//*[@id="thumbnailUL"]
        for div in coll_list:
            coll_name = div.xpath('./a/div/h2/text()').extract_first()
            print(coll_name)
            
            detail_url = 'http://www.changjiangcp.com' + div.xpath('./a/@href').extract_first()
            #coll_img = div.xpath('./div/a/@url').extract_first()
            #coll_img = 'http://www.changjiangcp.com' + coll_img
            #print(coll_img)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        
        if self.page_num <= 13:
            new_url = (self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)

    
        
