import scrapy
from museum.items import exhibitionItem

class Exhibition93Spider(scrapy.Spider):
    name = 'exhibition93'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.aybwg.org/anbozhanlan/list.php?catid=35']

    
    def parse_detail(self, response):
        item = response.meta["item"]
        
        if response.xpath('//*[@id="content"]/p//text()'):
            exhib_desc = response.xpath('//*[@id="content"]/p//text()').extract()
            exhib_desc = ''.join(exhib_desc)
            print(exhib_desc)  

    def parse(self, response):
        item = exhibitionItem()
        exhib_list = response.xpath('/html/body/div/div[4]/div[2]/ul/li')
        
        for li in exhib_list:
            #/a/div/div
            exhib_name = li.xpath('./a/div/div/text()').extract_first()
            print(exhib_name)
            detail_url = li.xpath('./a/@href').extract_first()
            #/html/body/div/div[4]/div[2]/ul/li[1]/a/img
            exhib_img = li.xpath('./a/img/@src').extract_first()
            
            #exhib_img = 'http://www.whgmbwg.com' + exhib_img
            print(exhib_img)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
