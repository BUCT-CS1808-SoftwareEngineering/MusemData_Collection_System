import scrapy
from museum.items import exhibitionItem
import re 
# scrapy crawl exhibition188

class Exhibition188Spider(scrapy.Spider):
    name = 'exhibition188'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://pjcmm.com/listPro.aspx?cateid=80']

    def parse(self, response):
        item = exhibitionItem()
        div_list = response.xpath('//ul[@class="listPro"]/li')
        num = 1
        for div in div_list:
            if num > 4:
                break
            num += 1
            img = "http://pjcmm.com" + div.xpath('./a/img/@src').extract_first()
            # img = 'http://www.portmuseum.cn' + img
            print(img)
            detail_url = "http://pjcmm.com/" + div.xpath('./a/@href').extract_first()
            # cont = div.xpath('./div/div[2]/span/text()').extract_first()
            # print(cont)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        
    
    def parse_detail(self, response):
        item = response.meta["item"]
        name = response.xpath('//div[@class="contentTitle"]/text()').extract_first()
        print(name)
        
        # exhib_name = response.xpath('/html/body/div[3]/div[1]/text()').extract_first()
        # print(exhib_name)
        # time = response.xpath('/html/body/div[3]/div[2]/div/div[2]/div[2]/p[2]/text()').extract()
        # time = ''.join(time)
        # loca = response.xpath('/html/body/div[3]/div[2]/div/div[2]/div[3]/p[2]/text()').extract()
        # loca = ''.join(loca)
        cont = response.xpath('/html/body/div[4]/div[2]/p//text()').extract()
        cont = ''.join(cont)
        print(cont)
