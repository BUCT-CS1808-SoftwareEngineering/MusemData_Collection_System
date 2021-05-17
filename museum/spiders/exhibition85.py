import scrapy
from museum.items import exhibitionItem

class Exhibition85Spider(scrapy.Spider):
    name = 'exhibition85'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.whgmbwg.com/clzl/jbcl2/index.shtml']

    def parse_detail(self, response):
        item = response.meta["item"]
        
        if response.xpath('/html/body/div[3]/div[5]/div/div[2]/p/span//text()'):
            exhib_desc = response.xpath('/html/body/div[3]/div[5]/div/div[2]/p/span//text()').extract()
            exhib_desc = ''.join(exhib_desc)
            print(exhib_desc)  

    def parse(self, response):
        item = exhibitionItem()
        exhib_list = response.xpath('/html/body/div[3]/div[5]/div[1]/ul/li')
        
        for li in exhib_list:
            
            exhib_name = li.xpath('./a/p/text()').extract_first()
            print(exhib_name)
            detail_url = 'http://www.whgmbwg.com' + li.xpath('./a/@href').extract_first()
            exhib_img = li.xpath('./a/img/@src').extract_first()
            
            exhib_img = 'http://www.whgmbwg.com' + exhib_img
            print(exhib_img)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        
        #if self.page_num <= 14:
        #    new_url = (self.url%self.page_num)
        #    self.page_num += 1
        #    yield scrapy.Request(new_url,callback=self.parse)
