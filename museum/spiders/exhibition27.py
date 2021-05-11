import scrapy
from museum.items import exhibitionItem
import re 
# scrapy crawl exhibition27

class Exhibition27Spider(scrapy.Spider):
    name = 'exhibition27'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.portmuseum.cn/doc/zl/lszl/index.shtml']

    def parse(self, response):
        item = exhibitionItem()
        div_list = response.xpath('/html/body/div[3]/div[2]/ul/li')
        for div in div_list:
            img = div.xpath('./a/img/@src').extract_first()
            img = 'http://www.portmuseum.cn' + img
            print(img)
            detail_url = "http://www.portmuseum.cn" + div.xpath('./a/@href').extract_first()
            # cont = div.xpath('./div/div[2]/span/text()').extract_first()
            # print(cont)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        
    
    def parse_detail(self, response):
        item = response.meta["item"]
        exhib_name = response.xpath('/html/body/div[3]/div[1]/text()').extract_first()
        print(exhib_name)
        # time = response.xpath('/html/body/div[3]/div[2]/div/div[2]/div[2]/p[2]/text()').extract()
        # time = ''.join(time)
        # loca = response.xpath('/html/body/div[3]/div[2]/div/div[2]/div[3]/p[2]/text()').extract()
        # loca = ''.join(loca)
        cont = response.xpath('/html/body/div[3]/div[3]//text()').extract()
        cont = ''.join(cont)
        print(cont)
