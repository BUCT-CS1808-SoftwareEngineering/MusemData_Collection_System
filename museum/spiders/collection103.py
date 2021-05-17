import scrapy
from museum.items import collectionItem
#输出为空
class Collection103Spider(scrapy.Spider):
    name = 'collection103'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.zqqbwg.com/pic.php?cid=17']

    #def parse_detail(self, response):
        #item = response.meta["item"]
         
        #if response.xpath('/html/body/div[6]/div/div/div[2]/div[2]/p//text()'):
            #coll_desc = response.xpath('/html/body/div[6]/div/div/div[2]/div[2]/p//text()').extract()
            #coll_desc = ''.join(coll_desc)
            #print(coll_desc)  

    def parse(self, response):
        item = collectionItem() 
        coll_name = response.xpath('/html/body/table[3]/tbody/tr/td[3]/table/tbody/tr/td/table/tbody/tr[3]/td/ul/li[1]/a[1]/p//text()').extract()
        coll_name = ''.join(coll_name)
        print(coll_name) 
        #/html/body/table[3]/tbody/tr/td[3]/table/tbody/tr/td/table/tbody/tr[3]/td/ul
        #coll_list = response.xpath('/html/body/table[3]/tbody/tr/td[3]/table/tbody/tr/td/table/tbody/tr[3]/td/ul/li')
        #for div in coll_list:
            #/html/body/table[3]/tbody/tr/td[3]/table/tbody/tr/td/table/tbody/tr[3]/td/ul
            #coll_name = div.xpath('./a/p//text()').extract()
            #coll_name = ''.join(coll_name)
            #print(coll_name) 
            #if div.xpath('./a/img/@src'):
               # coll_img = div.xpath('./a/img/@src').extract_first()
                #coll_img = 'http://www.kzbwg.cn' + coll_img
                #print(coll_img)
            #if div.xpath('./a/@href'):
                #detail_url = 'http://www.kzbwg.cn' + div.xpath('./a/@href').extract_first()
                #yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
            #yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})

