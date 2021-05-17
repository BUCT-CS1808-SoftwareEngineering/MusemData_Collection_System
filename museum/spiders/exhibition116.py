import scrapy
from museum.items import exhibitionItem

class Exhibition116Spider(scrapy.Spider):
    name = 'exhibition116'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.gzsbwg.cn/html/infolist-27.html']

    def parse(self, response):
        item = exhibitionItem()
        exhib_name = response.xpath('/html/body/div[5]/div/div[1]/div/div//text()').extract()
        exhib_name = ''.join(exhib_name)
        print(exhib_name)
