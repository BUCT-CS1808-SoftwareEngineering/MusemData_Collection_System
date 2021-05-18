import scrapy
from museum.items import exhibitionItem
import re 
# scrapy crawl exhibition193

class Exhibition193Spider(scrapy.Spider):
    name = 'exhibition193'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.printingmuseum.cn/Exhibitions/PExhibitionsList/BasicExhibition#comehere']

    def parse(self, response):
        item = exhibitionItem()
        div_list = response.xpath('//*[@id="ulBaseExhibitList"]/li')
        num = 1
        for div in div_list:
            if num > 6:
                break
            num += 1
            img = div.xpath('./div[1]/img/@src').extract_first()
            # img = 'http://www.portmuseum.cn' + img
            print(img)
            name = div.xpath('./div[1]/span/h3/text()').extract_first()
            print(name)
            detail_url = "http://www.printingmuseum.cn" + div.xpath('./div[2]/a/@href').extract_first()
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
        cont = response.xpath('//*[@id="divBaseExDetail"]/div[2]/p//text()').extract()
        cont = ''.join(cont)
        print(cont)
