import scrapy
from museum.items import exhibitionItem

#输出为空
class Exhibition112Spider(scrapy.Spider):
    name = 'exhibition112'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://museum.linyi.cn/clzl/lszl.htm']

    #def parse_detail(self, response):
        #item = response.meta["item"]
        
        #if response.xpath('/html/body/div[7]/div[2]/div[2]/div[2]/div[1]/div/p//text()'):
            #exhib_desc = response.xpath('/html/body/div[7]/div[2]/div[2]/div[2]/div[1]/div/p//text()').extract()
            #exhib_desc = ''.join(exhib_desc)
            #print(exhib_desc)  
            

    def parse(self, response):
        item = exhibitionItem()
       
        #exhib_list = response.xpath('/html/body/div[7]/div[2]/div[2]/div[1]/ul/li')
        exhib_name = response.xpath('/html/body/div[3]/div/div[2]/table[1]/tbody/tr/td/div/table/tbody/tr[1]/td[1]/span/a/span/text()').extract_first()
        print(exhib_name)
        #for li in exhib_list:
            #/html/body/div[7]/div[2]/div[2]/div[1]/ul/li[1]/a
            #exhib_name = li.xpath('./a/text()').extract_first()
            #print(exhib_name)
            #/html/body/div[7]/div[2]/div[2]/div[1]/ul/li[1]/div/a/img
            #exhib_img = li.xpath('./div/a/img/@src').extract_first()
            #exhib_img = 'http://www.wfsbwg.com' + exhib_img
            #print(exhib_img)
            #detail_url = 'http://www.wfsbwg.com' + li.xpath('./div//a/@href').extract_first()
            #yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})

