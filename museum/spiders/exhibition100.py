import scrapy
from museum.items import exhibitionItem
#详情页信息爬取为空
class Exhibition100Spider(scrapy.Spider):
    name = 'exhibition100'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.zbstcbwg.cn/specialExhibition.html']

    def parse_detail(self, response):
        item = response.meta["item"]
        #/html/body/div[4]/div[1]/div/div[2]/div[2]/div/div/div[1]/div[3]
        if response.xpath('/html/body/div[4]/div[1]/div/div[2]/div[2]/div/div/div[1]/div[3]//text()'):
            exhib_desc = response.xpath('/html/body/div[4]/div[1]/div/div[2]/div[2]/div/div/div[1]/div[3]//text()').extract()
            exhib_desc = ''.join(exhib_desc)
            print(exhib_desc)
            #print(response.xpath('/html/body/div[4]/div[1]/div/div[2]/div[2]/div/div/div[1]/div[2]/text()').extract_first())
            #print("2")  
        #print("1")
        #print(response.xpath('/html/body/div[4]/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/text()').extract_first())
    def parse(self, response):
        item = exhibitionItem()
        #/html/body/div[3]/div/div/div[4]/div[1]/div[1]
        exhib_list = response.xpath('/html/body/div[3]/div/div/div[4]/div[1]/div')
        
        for div in exhib_list:
            #/html/body/div[3]/div/div/div[4]/div[1]/div[1]/a
            exhib_name = div.xpath('./div[1]/div[2]/text()').extract_first()
            print(exhib_name)
            detail_url = 'http://www.zbstcbwg.cn' + div.xpath('./a/@href').extract_first()
            print(detail_url)
            exhib_img = div.xpath('./div[2]/img/@src').extract_first()
            
            exhib_img = 'http://www.zbstcbwg.cn' + exhib_img
            print(exhib_img)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
