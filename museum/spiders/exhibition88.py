import scrapy
from museum.items import exhibitionItem
#爬取数据为空
class Exhibition88Spider(scrapy.Spider):
    name = 'exhibition88'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://jzmsm.org/yk/zhanlan/badachenlie/']

    #def parse_detail(self, response):
        #item = response.meta["item"]
        
        #if response.xpath('/html/body/div[6]/div/div[3]/p/span//text()'):
            #exhib_desc = response.xpath('/html/body/div[3]/div[5]/div/div[2]/p/span//text()').extract()
            #exhib_desc = ''.join(exhib_desc)
            #print(exhib_desc)  

    def parse(self, response):
        item = exhibitionItem()
        #/html/body/div[3]/table[1]/tbody/tr[1]/td[1]/ul/table/tbody/tr/td[3]/table/tbody/tr[1]/td/a
        #/html/body/div[3]/table[1]/tbody/tr[1]/td[3]/ul/table/tbody/tr/td[3]/table/tbody/tr[1]/td/a
        #/html/body/div[3]/table[2]/tbody/tr[1]/td[1]/ul/table/tbody/tr/td[3]/table/tbody/tr[1]/td/a
        #/html/body/div[3]/table[2]/tbody/tr[1]/td[3]/ul/table/tbody/tr/td[3]/table/tbody/tr[1]/td/a
        #/html/body/div[3]/table[3]/tbody/tr[1]/td[1]/ul/table/tbody/tr/td[3]/table/tbody/tr[1]/td/a
         #1 由于分版块无法形成循环
        exhib_name = response.xpath('/html/body/div[3]/table[1]/tbody/tr[1]/td[1]/ul/table/tbody/tr/td[3]/table/tbody/tr[1]/td/a/text()').extract_first()
        print(exhib_name)
        #detail_url = 'http://jzmsm.org' + response.xpath('/html/body/div[3]/table[1]/tbody/tr[1]/td[1]/ul/table/tbody/tr/td[1]/a/@href').extract_first()
        img = response.xpath('/html/body/div[3]/table[1]/tbody/tr[1]/td[1]/ul/table/tbody/tr/td[1]/a/img/@src').extract_first()
                            #/html/body/div[3]/table[1]/tbody/tr[1]/td[3]/ul/table/tbody/tr/td[1]/a/img
        print(img)
        #yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
         #2
        exhib_name = response.xpath('/html/body/div[3]/table[1]/tbody/tr[1]/td[3]/ul/table/tbody/tr/td[3]/table/tbody/tr[1]/td/a/text()').extract_first()
        print(exhib_name)
        #http://jzmsm.org
        #detail_url = 'http://jzmsm.org' + response.xpath('/html/body/div[3]/table[1]/tbody/tr[1]/td[3]/ul/table/tbody/tr/td[1]/a/@href').extract_first()
        img = response.xpath('/html/body/div[3]/table[1]/tbody/tr[1]/td[3]/ul/table/tbody/tr/td[1]/a/img/@src').extract_first()
        #/html/body/div[3]/table[1]/tbody/tr[1]/td[3]/ul/table/tbody/tr/td[1]/a/img
        print(img)
        #yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        
        
        
        
            
    
    
