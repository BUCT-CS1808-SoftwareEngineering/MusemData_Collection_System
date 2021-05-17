import scrapy
from museum.items import exhibitionItem

class Exhibition87Spider(scrapy.Spider):
    name = 'exhibition87'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.ycbwg.com/web/exhibition/basicDisplay/list.shtml']
    #详情页动态加载没有描述
     

    def parse(self, response):
        item = exhibitionItem()
        #/html/body/div/div[1]/div[3]/div/div[2]/div[3]/div/ul
        #/html/body/div/div[1]/div[3]/div/div[2]/div[3]/div
        exhib_list = response.xpath('/html/body/div/div[1]/div[3]/div/div[2]/div[3]/div/ul/li')
        
        for li in exhib_list:
            #/html/body/div/div[1]/div[3]/div/div[2]/div[3]/div/ul/li[1]/div[2]/a/h5/span[1]
            exhib_name = li.xpath('./div[2]/a/h5/span[1]/text()').extract_first()
            print(exhib_name)
            exhib_img = li.xpath('./div[1]/a/img/@src').extract_first()
            exhib_img = 'http://www.ycbwg.com' + exhib_img
            print(exhib_img)
            #yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
