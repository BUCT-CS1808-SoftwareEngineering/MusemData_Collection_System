import scrapy
from museum.items import exhibitionItem 

    
#动态加载
class Exhibition82Spider(scrapy.Spider):
    name = 'exhibition82'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.changjiangcp.com/list/20.html']

    def parse(self, response):
        item = exhibitionItem() 
        p_list = response.xpath('/html/body/div[6]/div/div[1]/div[2]/div/p')
        for p in p_list:
            exhib_name = p.xpath('./span/strong//text()').extract()
            exhib_name = ''.join(exhib_name)
            print(exhib_name)
            #img = response.xpath('img/@src').extract_first()
            #print(img)
        #yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        