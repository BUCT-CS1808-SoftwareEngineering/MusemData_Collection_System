import scrapy
from museum.items import collectionItem

class Collection88Spider(scrapy.Spider):
    name = 'collection88'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://jzmsm.org/yk/cangpin/guobaoxinshang/']

    def parse_detail(self, response):
        item = response.meta["item"]
        #//*[@id="divContent"]
                            #/html/body/div[6]/div/div[3]/p[5]/font/font/span/font/font/font
                            #/html/body/div[6]/div/div[3]/p[5]/font/font
                           #/html/body/div[6]/div/div[3]/p[5]/font/font/span/font/font/font
                           #/html/body/div[6]/div/div[3]/p[5]/font/font/span/font/font/font
                           #/html/body/div[6]/div/div[3]/p[5]/font/font
        if response.xpath('/html/body/div[6]/div/div[3]/p[5]/font/font//text()'):
            coll_desc = response.xpath('/html/body/div[6]/div/div[3]/p[5]/font/font//text()').extract()
            coll_desc = ''.join(coll_desc)
            print(coll_desc)  

    def parse(self, response):
        item = collectionItem()
        coll_list = response.xpath('/html/body/div[3]/ul/li')
        #//*[@id="thumbnailUL"]
        for li in coll_list:
            #/a[2]
            coll_name = li.xpath('./a[2]/text()').extract_first()
            print(coll_name)
            detail_url = 'http://jzmsm.org' + li.xpath('./a[1]/@href').extract_first()
            coll_img = li.xpath('./a[1]/img/@src').extract_first()
            #http://61.187.53.122/
            coll_img = 'http://jzmsm.org' + coll_img
            print(coll_img)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
    
