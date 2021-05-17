import scrapy
from museum.items import exhibitionItem 


class Exhibition81Spider(scrapy.Spider):
    name = 'exhibition81'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.hnmuseum.com/zh-hans/content/%E5%BD%93%E5%89%8D%E5%B1%95%E8%A7%88%EF%BC%8D%E5%9F%BA%E6%9C%AC%E9%99%88%E5%88%97']

    def parse_detail(self, response):
        item = response.meta["item"]       
        cont = response.xpath('/html/body/div[3]/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/p//text()').extract()
        cont = ''.join(cont)
        print(cont)
     

    def parse(self, response):
        item = exhibitionItem()  
         #1 由于分版块无法形成循环
        exhib_name = response.xpath('/html/body/div[3]/div[1]/div[1]/div[2]/div[3]/div[2]/div/div/div/div[1]/h3/span/a/text()').extract_first()
        print(exhib_name)
        detail_url = 'http://www.hnmuseum.com' + response.xpath('/html/body/div[3]/div[1]/div[1]/div[2]/div[3]/div[2]/div/div/div/div[1]/div[1]/div/a/@href').extract_first()
        img = response.xpath('/html/body/div[3]/div[1]/div[1]/div[2]/div[3]/div[2]/div/div/div/div[1]/div[1]/div/a/img/@src').extract_first()
        print(img)
        yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
         #2
        exhib_name = response.xpath('/html/body/div[3]/div[1]/div[1]/div[2]/div[3]/div[2]/div/div/div/div[2]/h3/span/a/text()').extract_first()
        print(exhib_name)
        detail_url = 'http://www.hnmuseum.com' + response.xpath('/html/body/div[3]/div[1]/div[1]/div[2]/div[3]/div[2]/div/div/div/div[2]/div[1]/div/a/@href').extract_first()
        img = response.xpath('/html/body/div[3]/div[1]/div[1]/div[2]/div[3]/div[2]/div/div/div/div[2]/div[1]/div/a/img/@src').extract_first()
        print(img)
        yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        #3
        exhib_name = response.xpath('/html/body/div[3]/div[1]/div[1]/div[2]/div[3]/div[3]/div/div/div/div[1]/h3/span/a/text()').extract_first()
        print(exhib_name)
        detail_url = 'http://www.hnmuseum.com' + response.xpath('/html/body/div[3]/div[1]/div[1]/div[2]/div[3]/div[3]/div/div/div/div[1]/div[1]/div/a/@href').extract_first()
        img = response.xpath('/html/body/div[3]/div[1]/div[1]/div[2]/div[3]/div[3]/div/div/div/div[1]/div[1]/div/a/img/@src').extract_first()
        print(img)
        yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        #4
        exhib_name = response.xpath('/html/body/div[3]/div[1]/div[1]/div[2]/div[3]/div[3]/div/div/div/div[2]/h3/span/a/text()').extract_first()
        print(exhib_name)
        detail_url = 'http://www.hnmuseum.com' + response.xpath('/html/body/div[3]/div[1]/div[1]/div[2]/div[3]/div[3]/div/div/div/div[2]/div[1]/div/a/@href').extract_first()
        img = response.xpath('/html/body/div[3]/div[1]/div[1]/div[2]/div[3]/div[3]/div/div/div/div[2]/div[1]/div/a/img/@src').extract_first()
        print(img)
        yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        #5
        exhib_name = response.xpath('/html/body/div[3]/div[1]/div[1]/div[2]/div[3]/div[3]/div/div/div/div[3]/h3/span/a/text()').extract_first()
        print(exhib_name)
        detail_url = 'http://www.hnmuseum.com' + response.xpath('/html/body/div[3]/div[1]/div[1]/div[2]/div[3]/div[3]/div/div/div/div[3]/div[1]/div/a/@href').extract_first()
        img = response.xpath('/html/body/div[3]/div[1]/div[1]/div[2]/div[3]/div[3]/div/div/div/div[3]/div[1]/div/a/img/@src').extract_first()
        print(img)
        yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})