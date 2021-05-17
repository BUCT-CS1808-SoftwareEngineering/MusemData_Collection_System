import scrapy
from museum.items import collectionItem
#爬取数据为空
class Collection98Spider(scrapy.Spider):
    name = 'collection98'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.lymuseum.com/list.php?fid=45']

    def parse_detail(self, response):
        item = response.meta["item"]
        #/html/body/div[4]/ul/div[2]/li[2]/p    
        if response.xpath('/html/body/div[6]/div[4]/div[1]/div[9]/div/table/tbody/tr[2]/td/table[1]/tbody/tr/td/div/span//text()'):
            coll_desc = response.xpath('/html/body/div[6]/div[4]/div[1]/div[9]/div/table/tbody/tr[2]/td/table[1]/tbody/tr/td/div/span//text()').extract()
            coll_desc = ''.join(coll_desc)
            print(coll_desc)  

    def parse(self, response):
        item = collectionItem()  
        
        coll_list = response.xpath('/html/body/div[6]/div[4]/div[1]/div[9]/div/table/tbody/tr[1]/td/table/tbody/tr/td/div')
       
        for div in coll_list:
            #/p[2]/a
            coll_name = div.xpath('./p[2]/a/text()').extract_first()
            print(coll_name)

            #/html/body/div[6]/div[4]/div[1]/div[9]/div/table/tbody/tr[1]/td/table/tbody/tr/td/div[1]/p[1]/a/img
            coll_img = div.xpath('./p[1]/a/img/@src').extract_first()
            #coll_img = 'http://www.hnzzmuseum.com' + coll_img
            print(coll_img)
            #/html/body/div[6]/div[4]/div[1]/div[9]/div/table/tbody/tr[1]/td/table/tbody/tr/td/div[1]/p[1]/a
            detail_url = 'http://www.lymuseum.com/' + div.xpath('./p[1]/a/@href').extract_first()

            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
