import scrapy
from museum.items import exhibitionItem
#动态加载
class Exhibition83Spider(scrapy.Spider):
    name = 'exhibition83'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.zhongshanwarship.org.cn/zhanlan.html']

    #def parse_detail(self, response):
        #item = response.meta["item"]
        
        #if response.xpath('/html/body/div[3]/div[5]/div/div[2]/p/span//text()'):
            #exhib_desc = response.xpath('/html/body/div[3]/div[5]/div/div[2]/p/span//text()').extract()
           # exhib_desc = ''.join(exhib_desc)
           # print(exhib_desc)  

    def parse(self, response):
        item = exhibitionItem()
        exhib_list = response.xpath('//*[@id="caseListDIV"]/div')
        
        for li in exhib_list:
            
            exhib_name = li.xpath('./div/a/span/text()').extract_first()
            print(exhib_name)
           # detail_url = 'http://www.whgmbwg.com' + li.xpath('./a/@href').extract_first()
           # exhib_img = li.xpath('./a/img/@src').extract_first()
            #
           # exhib_img = 'http://www.whgmbwg.com' + exhib_img
            #print(exhib_img)
           # yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
       
