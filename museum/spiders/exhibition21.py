import scrapy
from museum.items import exhibitionItem
import re 
# scrapy crawl exhibition21

class Exhibition21Spider(scrapy.Spider):
    name = 'exhibition21'
    start_urls = ['http://www.bjqtm.com/clzl/lszl/']

    def parse(self, response):
        item = exhibitionItem()
        div_list = response.xpath('/html/body/div[4]/div/div[2]/div[2]/div[1]/ul/li')
        for div in div_list:
            detail_url = div.xpath('./a/@href').extract_first()
            detail_url = 'http://www.bjqtm.com' + detail_url
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
    
    def parse_detail(self, response):
        item = response.meta["item"]
        exhib_name = response.xpath('/html/body/div[4]/div/div[2]/div[2]/h2/text()').extract_first()
        print(exhib_name)
        img = response.xpath('/html/body/div[4]/div/div[2]/div[2]/div[1]//img/@src').extract_first()
        img = ''.join(img)
        img = 'http://www.bjqtm.com' + img
        print(img)
        cont = response.xpath('/html/body/div[4]/div/div[2]/div[2]/div[1]//text()').extract()
        cont = ''.join(cont)
        cont = re.sub('\s','',cont)
        if cont == "点击此处查看详情":
            cont = "None" 
        print(cont)
        # yield item
