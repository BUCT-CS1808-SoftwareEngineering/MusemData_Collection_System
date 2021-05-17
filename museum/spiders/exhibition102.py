import scrapy
from museum.items import exhibitionItem
#由于网页中详情页的网址内容多加了.. 图片多加了一个空格，所以无法解析
class Exhibition102Spider(scrapy.Spider):
    name = 'exhibition102'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://museum.sdu.edu.cn/clzl/cszl.htm']

    #def parse_detail(self, response):
        #item = response.meta["item"]
        
        #if response.xpath('/html/body/div[2]/div[2]/form/div[2]/div/p//text()'):
            #exhib_desc = response.xpath('/html/body/div[2]/div[2]/form/div[2]/div/p//text()').extract()
            #exhib_desc = ''.join(exhib_desc)
            #print(exhib_desc)  

    def parse(self, response):
        item = exhibitionItem()
        exhib_list = response.xpath('//*[@id="c"]/div')
        for div in exhib_list:
            
            exhib_name = div.xpath('./div[2]/a/@title').extract_first()
            print(exhib_name)
            #if div.xpath('./div[2]/a/@href'):
            #   detail_url = 'http://museum.sdu.edu.cn' + div.xpath('./div[2]/a/@href').extract_first()
            #   yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
            if div.xpath('./div[2]/a/img/@src'):
            #http://museum.sdu.edu.cn
                exhib_img = 'http://museum.sdu.edu.cn' + div.xpath('./div[2]/a/img/@src').extract_first()            
                print(exhib_img)
            
