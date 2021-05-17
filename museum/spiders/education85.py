import scrapy
from museum.items import educationItem

class Education85Spider(scrapy.Spider):
    name = 'education85'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://mp.weixin.qq.com/s/iYQuPlJXNNP1tOlwKNy4fQ']

    def parse(self, response):
        #//*[@id="activity-name"]
        name = response.xpath('//*[@id="activity-name"]//text()').extract()
        name = ''.join(name)
        print(name)
        img = response.xpath('/html/body/div[1]/div[2]/div[1]/div/div[1]/div[3]/section/section[5]/section/img/@data-src').extract()
        img = ''.join(img)
        print(img)
        cont = response.xpath('/html/body/div[1]/div[2]/div[1]/div/div[1]/div[3]/section/section[3]/section/section/section/p//text()').extract()
        cont = ''.join(cont)
        print(cont)
