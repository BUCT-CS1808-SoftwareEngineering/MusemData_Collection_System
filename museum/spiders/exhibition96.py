import scrapy
from museum.items import exhibitionItem

class Exhibition96Spider(scrapy.Spider):
    name = 'exhibition96'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.hnzzmuseum.com/display9_list.html']

    def parse(self, response):
        item = exhibitionItem()
        
        exhib_list = response.xpath('/html/body/div[4]/div')
        
        for div in exhib_list:
            #/html/body/div[4]/div[1]/ul/li/a/p[1]
            exhib_name = div.xpath('./ul/li/a/p[1]//text()').extract()
            exhib_name = ''.join(exhib_name)
            print(exhib_name)
            #/html/body/div[4]/div[1]/ul/img
            exhib_img = div.xpath('./ul/img/@src').extract_first()
            
            exhib_img = 'http://www.hnzzmuseum.com' + exhib_img
            print(exhib_img)  
            #/html/body/div[4]/div[1]/ul/li/a/p[2]/span 
            exhib_desc = div.xpath('./ul/li/a/p[2]/span//text()').extract()
            exhib_desc = ''.join(exhib_desc)
            print(exhib_desc)  