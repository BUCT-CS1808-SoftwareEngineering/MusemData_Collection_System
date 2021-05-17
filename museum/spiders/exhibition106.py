import scrapy
from museum.items import exhibitionItem
#无描述信息
class Exhibition106Spider(scrapy.Spider):
    name = 'exhibition106'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.jiningmuseum.com/list/article_list.do?channelId=207']

    def parse(self, response):
        item = exhibitionItem()
       
        exhib_list = response.xpath('/html/body/div[3]/div[2]/div[1]/ul/li')
        for li in exhib_list:
            #/html/body/div[3]/div[2]/div[1]/ul/li[1]/a/div[2]/h3
            exhib_name = li.xpath('./a/div[2]/h3/text()').extract_first()
            print(exhib_name)
            #/html/body/div[3]/div[2]/div[1]/ul/li[1]/a/div[1]/img
            exhib_img = li.xpath('./a/div[1]/img/@src').extract_first()
            print(exhib_img)
           