import scrapy
from museum.items import exhibitionItem
#详情页无输出
class Exhibition107Spider(scrapy.Spider):
    name = 'exhibition107'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.ytmuseum.com/showroom/jb']

    def parse_detail(self, response):
        item = response.meta["item"]
        
        if response.xpath('/html/body/div[3]/div[2]/div/div/div[4]/div[1]/table/tbody/tr[3]/td/p[4]/span//text()'):
            exhib_desc = response.xpath('/html/body/div[3]/div[2]/div/div/div[4]/div[1]/table/tbody/tr[3]/td/p[4]/span//text()').extract()
            exhib_desc = ''.join(exhib_desc)
            print(exhib_desc)  
            print("2")
        #print("1")

    def parse(self, response):
        item = exhibitionItem()
       
        exhib_list = response.xpath('/html/body/div[3]/div[2]/div/div/div[4]/div/ul/li')
        
        for li in exhib_list:
            #/html/body/div[3]/div[2]/div/div/div[4]/div/ul/li[1]/div[2]/a
            exhib_name = li.xpath('./div[2]/a/text()').extract_first()
            print(exhib_name)
            #/html/body/div[3]/div[2]/div/div/div[4]/div/ul/li[1]/div[1]/a/img
            exhib_img = li.xpath('./div[1]/a/img/@src').extract_first()
            exhib_img = 'http:' + exhib_img
            print(exhib_img)
            detail_url = 'http://www.ytmuseum.com' + li.xpath('./div[1]/a/@href').extract_first()
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})

