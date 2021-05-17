import scrapy
from museum.items import exhibitionItem
#展馆无描述信息
class Exhibition92Spider(scrapy.Spider):
    name = 'exhibition92'
    allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.wzbwg.com/news/22']

    #def parse_detail(self, response):
        #item = response.meta["item"]
        
        #if response.xpath('/html/body/div[3]/div[4]/p//text()'):
            #exhib_desc = response.xpath('/html/body/div[3]/div[4]/p//text()').extract()
            #exhib_desc = ''.join(exhib_desc)
            #print(exhib_desc)  

    def parse(self, response):
        item = exhibitionItem()
        exhib_list = response.xpath('//*[@id="cxList"]/li')
        
        for li in exhib_list:
            #/p/a
            exhib_name = li.xpath('./a/@title').extract_first()
            print(exhib_name)
            #detail_url = 'http://www.pdsm.org.cn' + li.xpath('./a/@href').extract_first()
            #/html/body/div[3]/div[3]/ul/li[1]/a/img
            exhib_img = li.xpath('./a/div/img/@src').extract_first()
            exhib_img = 'http://www.wzbwg.com' + exhib_img
            print(exhib_img)
            #yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
    
