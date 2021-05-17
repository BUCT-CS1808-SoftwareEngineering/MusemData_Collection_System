import scrapy
from museum.items import collectionItem
#空
class Collection118Spider(scrapy.Spider):
    name = 'collection118'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.lushanmuseum.com/jingpin.asp?id=34']

    url = 'http://www.lushanmuseum.com/jingpin.asp?id=34&page=%d'
    page_num = 2

    def parse_detail(self, response):
        item = response.meta["item"]    
        if response.xpath('/html/body/table[4]/tbody/tr/td[3]/table/tbody/tr[2]/td/span/text()'):
            coll_name = response.xpath('/html/body/table[4]/tbody/tr/td[3]/table/tbody/tr[2]/td/span/text()').extract_first()
            print(coll_name)
             

    def parse(self, response):
        item = collectionItem()          
        coll_list = response.xpath('/html/body/table[4]/tbody/tr/td[3]/table/tbody/tr[4]/td/ul/li')
        #/html/body/div[3]/div/div[2]/table[1]/tbody/tr/td/div/table/tbody/tr[1]/td[1]
        for div in coll_list:
            coll_img =  'http://www.lushanmuseum.com' + div.xpath('./a/img/@src').extract_first()          
            print(coll_img)
           
            detail_url = 'http://www.lushanmuseum.com' + div.xpath('./a/@href').extract_first()
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        if self.page_num <= 3:
            new_url = (self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)


