import scrapy
from museum.items import exhibitionItem

class Exhibition120Spider(scrapy.Spider):
    name = 'exhibition120'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.qingdaomuseum.com/exhibition/category/16']

    def parse_detail(self, response):
        item = response.meta["item"]
        
        if response.xpath('/html/body/div[6]/div[2]/div/div[4]/p//text()'):
            exhib_desc = response.xpath('/html/body/div[6]/div[2]/div/div[4]/p//text()').extract()
            exhib_desc = ''.join(exhib_desc)
            print(exhib_desc)  
            

    def parse(self, response):
        item = exhibitionItem()
       
        exhib_list = response.xpath('/html/body/div[6]/div[2]/div[2]/div[1]/div')
        
        for li in exhib_list:
            #/html/body/div[6]/div[2]/div[2]/div[1]/div[1]/div/a/div/h4
            exhib_name = li.xpath('./div/a/div/h4/text()').extract_first()
            print(exhib_name)
            #/html/body/div[6]/div[2]/div[2]/div[1]/div[1]/div/a/img
            exhib_img = li.xpath('./div/a/img/@src').extract_first()
            #exhib_img = 'http://www.wfsbwg.com' + exhib_img
            print(exhib_img)
            detail_url =  li.xpath('./div/a/@href').extract_first()
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
