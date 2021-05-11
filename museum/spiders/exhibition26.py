import scrapy
from museum.items import exhibitionItem
import re 
# scrapy crawl exhibition26

class Exhibition26Spider(scrapy.Spider):
    name = 'exhibition26'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.njiemuseum.com/index.php/Index/Index/col/c_id/41.html']

    def parse(self, response):
        item = exhibitionItem()
        div_list = response.xpath('//*[@id="ContentPlaceHolder1_main_cnt"]/ul/li')
        num = 1
        for div in div_list:
            if num > 6:
                break
            num += 1
            exhib_name = div.xpath('./div/div[2]/a[1]/h1/text()').extract_first()
            print(exhib_name)
            img = div.xpath('./div/div[1]/img/@src').extract_first()
            img = 'http://www.njiemuseum.com' + img
            print(img)
            detail_url = "https://www.cdmuseum.com" + div.xpath('./div/div[2]/a[1]/@href').extract_first()
            cont = div.xpath('./div/div[2]/span/text()').extract_first()
            print(cont)
            # yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        
    
    # def parse_detail(self, response):
    #     item = response.meta["item"]
    #     # time = response.xpath('/html/body/div[3]/div[2]/div/div[2]/div[2]/p[2]/text()').extract()
    #     # time = ''.join(time)
    #     # loca = response.xpath('/html/body/div[3]/div[2]/div/div[2]/div[3]/p[2]/text()').extract()
    #     # loca = ''.join(loca)
    #     cont = response.xpath('//*[@id="ContentPlaceHolder1_cnt"]/div/div/div[5]/section/section[1]/section[1]/section/section/section/section//text()').extract()
    #     cont = ''.join(cont)
    #     cont = "\n时间：" + time + " 地点：" + loca + cont
    #     print(cont)
