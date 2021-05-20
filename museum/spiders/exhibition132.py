import scrapy
from museum.items import exhibitionItem 
#scrapy crawl collection
#scrapy crawl exhiition
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
#scrapy genspider education
class Education9Spider(scrapy.Spider):
    name = 'exhibition132'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.fjbwy.com/node_22.html']

    def parse(self, response):
        item = exhibitionItem()
        #scrapy crawl exhibition132
        div_list = response.xpath('//*[@class="zp_k"]')
        for li in div_list:
             name = li.xpath('./div[2]//span/text()').extract_first()
             print(name)
             img=li.xpath('.//img/@src').extract_first()
             #img='http://www.qzhjg.cn'+img
             print(img)
             detail_url=li.xpath('.//a/@href').extract_first()
             #detail_url='http://www.qzhjg.cn'+detail_url
             print(detail_url)
             yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
    def parse_detail(self, response):
        item = response.meta["item"]
        #img = response.xpath('//*[@class="nr"]//img/@src').extract_first()
        #print(img)
        cont=response.xpath('//*[@class="zw"]//text()').extract()+response.xpath('//*[@class="neir_zw"]//text()').extract()
        cont = ''.join(cont)
        print(cont)