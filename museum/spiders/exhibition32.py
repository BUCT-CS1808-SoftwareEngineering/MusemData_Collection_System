import scrapy
from museum.items import exhibitionItem
import re 
# scrapy crawl exhibition32

class Exhibition32Spider(scrapy.Spider):
    name = 'exhibition32'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.nxbwg.com/c/lszl.html']

    def parse(self, response):
        item = exhibitionItem()
        div_list = response.xpath('//*[@id="content-container"]/div[2]/div[2]/main/div/div/div/article')
        for div in div_list:
            name = div.xpath('./div[1]/h3/a/text()').extract_first()
            print(name)
            img = div.xpath('./div[2]/div[1]/img/@src').extract_first()
            # img = 'http://www.portmuseum.cn' + img
            print(img)
            cont = div.xpath('./div[2]/div[2]//text()').extract()
            cont = ''.join(cont)
            # cont = div.xpath('./div/div[2]/span/text()').extract_first()
            print(cont)
            # yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
