import scrapy
from museum.items import educationItem

class Education81Spider(scrapy.Spider):
    name = 'education81'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.hnmuseum.com/zh-hans/audlts']

   
    def parse(self, response):
        item = educationItem()

        name = response.xpath('/html/body/div[3]/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div/p[2]/strong/text()').extract_first()
        #name = ''.join(name)
        print(name)

        img = response.xpath('/html/body/div[3]/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div/p[3]/img/@src').extract()
        img = ''.join(img)
        img = 'http://www.hnmuseum.com' + img
        print(img)
        cont = response.xpath('/html/body/div[3]/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div/p[3]//text()').extract()
        cont = ''.join(cont)
        print(cont)

        