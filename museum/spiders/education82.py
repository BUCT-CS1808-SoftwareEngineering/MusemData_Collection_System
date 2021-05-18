import scrapy
from museum.items import educationItem
#爬不出来数据none
class Education82Spider(scrapy.Spider):
    name = 'education82'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.changjiangcp.com/view/16384.html']

    def parse(self, response):
        item = educationItem()
        #/html/body/div[5]/div/div[1]/div/div[1]
        #/html/body/div[5]/div/div[1]/div/div[1]/h2
        #/html/body/div[5]/div/div[1]/div/div[1]/h2
        name = response.xpath('/html/body/div[5]/div/div[1]/div/div[1]/h2//text()').extract()
        name = ''.join(name)
        print(name)

