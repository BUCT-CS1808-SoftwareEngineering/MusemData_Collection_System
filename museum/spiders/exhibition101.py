import scrapy
from museum.items import exhibitionItem
#名称为none
class Exhibition101Spider(scrapy.Spider):
    name = 'exhibition101'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.qdyzyzmuseum.com/Home/Zhanlan/index/cateid/48']

    def parse_detail(self, response):
        item = response.meta["item"]
        #/html/body/div[5]/div/div/div[2]/h3
        
        if response.xpath('/html/body/div[5]/div/div/div[2]/div/div/p/img/@src'):
            exhib_img = 'http://www.qdyzyzmuseum.com'+response.xpath('/html/body/div[5]/div/div/div[2]/div/div/p/img/@src').extract_first()
            print(exhib_img)
        if response.xpath('/html/body/div[5]/div/div/div[2]/div/div/p//text()'):
            exhib_desc = response.xpath('/html/body/div[5]/div/div/div[2]/div/div/p//text()').extract()
            exhib_desc = ''.join(exhib_desc)
            print(exhib_desc)
           
    def parse(self, response):
        item = exhibitionItem()
        if(response.xpath('/html/body/div[5]/div/div/div[2]/div')):
            exhib_list = response.xpath('/html/body/div[5]/div/div/div[2]/div')
        
        for div in exhib_list:
            #/html/body/div[5]/div/div/div[2]/div[1]/a[1]/p/font
         
            exhib_name = div.xpath('./a[1]/p/font/text()').extract_first()
            print(exhib_name)
            if div.xpath('./a[1]/@href'):
                detail_url = 'http://www.qdyzyzmuseum.com' + div.xpath('./a/@href').extract_first()
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
