import scrapy
from museum.items import collectionItem
#输出为空
class Collection116Spider(scrapy.Spider):
    name = 'collection116'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.gzsbwg.cn/html/infolist-4-1.html']

    def parse(self, response):
        item = collectionItem()          
        #coll_list = response.xpath('/html/body/div[5]/div/div')
        coll_name = response.xpath('/html/body/div[5]/div/div[2]/a[1]/text()').extract_first()
        print(coll_name)
        #/html/body/div[3]/div/div[2]/table[1]/tbody/tr/td/div/table/tbody/tr[1]/td[1]
        #for div in coll_list:
            #/html/body/div[5]/div/div[2]/a[1]
            #coll_name = div.xpath('./a[1]/text()').extract_first()
            #print(coll_name)
            #table/tbody/tr/td/div/a/img
            #coll_img = '' + div.xpath('./table/tbody/tr/td/div/a/img/@src').extract_first()          
            #print(coll_img)
           
            #detail_url = '' + div.xpath('./table/tbody/tr/td/div/a/@href').extract_first()
            #yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})

