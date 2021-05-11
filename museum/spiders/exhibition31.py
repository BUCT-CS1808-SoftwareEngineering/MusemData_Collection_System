import scrapy
from museum.items import exhibitionItem
import re 
# scrapy crawl exhibition31

class Exhibition31Spider(scrapy.Spider):
    name = 'exhibition31'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.nxgybwg.com/e/action/ListInfo/?classid=14']

    def parse(self, response):
        item = exhibitionItem()
        div_list = response.xpath('//*[@id="body_wrap"]/div/div[2]/div[2]/div[2]/dl')
        for div in div_list:
            name = div.xpath('./dt/a/text()').extract_first()
            print(name)
            img = div.xpath('./dd[1]/a/img/@src').extract_first()
            # img = 'http://www.portmuseum.cn' + img
            print(img)
            detail_url = "http://www.nxgybwg.com" + div.xpath('./dt/a/@href').extract_first()
            # cont = div.xpath('./div/div[2]/span/text()').extract_first()
            # print(cont)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        
    
    def parse_detail(self, response):
        item = response.meta["item"]
        # exhib_name = response.xpath('/html/body/div[3]/div[1]/text()').extract_first()
        # print(exhib_name)
        # time = response.xpath('/html/body/div[3]/div[2]/div/div[2]/div[2]/p[2]/text()').extract()
        # time = ''.join(time)
        # loca = response.xpath('/html/body/div[3]/div[2]/div/div[2]/div[3]/p[2]/text()').extract()
        # loca = ''.join(loca)
        cont = response.xpath('//*[@id="body_wrap"]/div/div[2]/div[2]/div/div[2]/div//text()').extract()
        cont = ''.join(cont)
        print(cont)
