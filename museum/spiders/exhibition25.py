import scrapy
from museum.items import exhibitionItem
import re 
# scrapy crawl exhibition25

class Exhibition25Spider(scrapy.Spider):
    name = 'exhibition25'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.cdmuseum.com/linzhan/']

    def parse(self, response):
        item = exhibitionItem()
        div_list = response.xpath('/html/body/div[3]/div[2]/div/ul/li')
        num = 1
        for div in div_list:
            if num > 6:
                break
            num += 1
            exhib_name = div.xpath('./a/div[2]/div[1]/p/text()').extract_first()
            print(exhib_name)
            img = div.xpath('./a/div[1]/img/@src').extract_first()
            img = 'https://www.cdmuseum.com' + img
            print(img)
            detail_url = "https://www.cdmuseum.com" + div.xpath('./a/@href').extract_first()
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        
    
    def parse_detail(self, response):
        item = response.meta["item"]
        time = response.xpath('/html/body/div[3]/div[2]/div/div[2]/div[2]/p[2]/text()').extract()
        time = ''.join(time)
        loca = response.xpath('/html/body/div[3]/div[2]/div/div[2]/div[3]/p[2]/text()').extract()
        loca = ''.join(loca)
        cont = response.xpath('/html/body/div[3]/div[4]/div/div/div[2]/div//text()').extract()
        cont = ''.join(cont)
        cont = "\n时间：" + time + " 地点：" + loca + cont
        print(cont)
