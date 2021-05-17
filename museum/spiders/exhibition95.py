import scrapy
from museum.items import exhibitionItem

class Exhibition95Spider(scrapy.Spider):
    name = 'exhibition95'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.eywsqsfbwg.com/index.php?m=content&c=index&a=show&catid=11&id=45']

    def parse(self, response):
        item = exhibitionItem()
        
           
        exhib_name = response.xpath('/html/body/div[4]/div[2]/div/h2//text()').extract()
        exhib_name = ''.join(exhib_name)
        print(exhib_name)
        
        exhib_desc = response.xpath('//*[@id="conbox"]/p//text()').extract()
        exhib_desc = ''.join(exhib_desc)
        print(exhib_desc)  
        exhib_img = response.xpath('/html/body/div[4]/div[2]/div/div[1]/p[1]/img[1]/@src').extract_first()
        exhib_img = 'http://www.eywsqsfbwg.com/' + exhib_img
        print(exhib_img)
