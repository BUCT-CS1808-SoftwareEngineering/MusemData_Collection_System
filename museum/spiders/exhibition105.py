import scrapy
from museum.items import exhibitionItem

class Exhibition105Spider(scrapy.Spider):
    name = 'exhibition105'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.kzbwg.cn/zhanlan/jbcl/']

    def parse_detail(self, response):
        item = response.meta["item"]
        
        if response.xpath('/html/body/div[6]/div/div[1]/div/p//text()'):
            exhib_desc = response.xpath('/html/body/div[6]/div/div[1]/div/p//text()').extract()
            exhib_desc = ''.join(exhib_desc)
            print(exhib_desc)  

    def parse(self, response):
        item = exhibitionItem()
       
        exhib_list = response.xpath('/html/body/div[6]/div/div/div[4]/ul/li')
        
        for li in exhib_list:
           #div/h3/a
            exhib_name = li.xpath('./div/h3/a/text()').extract_first()
            print(exhib_name)
            exhib_img = li.xpath('./a/img/@src').extract_first()
            exhib_img = 'http://www.kzbwg.cn' + exhib_img
            print(exhib_img)
            detail_url = 'http://www.kzbwg.cn' + li.xpath('./a/@href').extract_first()
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
