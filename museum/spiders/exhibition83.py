import scrapy
from museum.items import exhibitionItem
#动态加载
class Exhibition83Spider(scrapy.Spider):
    name = 'exhibition83'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.changjiangcp.com/list/19.html']

    def parse(self, response):
        item = exhibitionItem()
        #cont = response.xpath('/html/body/div[6]/div/div[1]/div[2]/div/p[2]/span/span/span//text()').extract()
        cont = ''.join(cont)
        print(cont)
