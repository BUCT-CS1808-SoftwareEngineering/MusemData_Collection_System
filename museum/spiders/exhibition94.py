import scrapy
from museum.items import exhibitionItem

class Exhibition94Spider(scrapy.Spider):
    name = 'exhibition94'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.kfsbwg.com/html/zhanlan/jbcl/']
    #详情页数据无法解析缺少描述信息
    def parse_detail(self, response):
        item = response.meta["item"]
        
        if response.xpath('/html/body/div[3]/div[2]/div/p[3]//text()'):
            exhib_desc = response.xpath('/html/body/div[3]/div[2]/div/p[3]//text()').extract()
            exhib_desc = ''.join(exhib_desc)
            print(exhib_desc)
            #print("2")
        #print("1")  

    def parse(self, response):
        item = exhibitionItem()
        exhib_list = response.xpath('/html/body/div[2]/div[2]/ul/li')
        
        for li in exhib_list:
            #/html/body/div[2]/div[2]/ul/li[1]/p[1]
            exhib_name = li.xpath('./p[1]//text()').extract()
            exhib_name = ''.join(exhib_name)
            print(exhib_name)
            detail_url = li.xpath('./div/a/@href').extract_first()
            #/html/body/div[2]/div[2]/ul/li[1]/div/a/img
            exhib_img = li.xpath('./div/a/img/@src').extract_first()
            
            #exhib_img = 'http://www.whgmbwg.com' + exhib_img
            print(exhib_img)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
