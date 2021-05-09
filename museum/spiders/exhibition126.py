import scrapy
from museum.items import exhibitionItem 
#scrapy crawl collection
#scrapy crawl exhiition
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
#scrapy genspider education
class Exhibition126Spider(scrapy.Spider):
    name = 'exhibition126'
    #allowed_domains = ['www.ccc.com']
    start_urls = ['http://www.81-china.com/zhanlan/57.html']

    def parse(self, response):
        item = exhibitionItem()
        #scrapy crawl exhibition126
        div_list = response.xpath('//*[@class="list_ul"]/li')
        for li in div_list:
            name = li.xpath('./div[2]/h3//text()').extract_first()
            print(name)
            detail_url=li.xpath('./div[1]/a/@href').extract_first()
            detail_url='http://www.81-china.com'+detail_url
            print(detail_url)
            img=li.xpath('./div[1]/a/img/@src').extract_first()
            img='http://www.81-china.com'+img
            print(img)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
    def parse_detail(self, response):
        item = response.meta["item"]
        #img = response.xpath('//*[@class="nr"]//img/@src').extract_first()
        #print(img)
        cont=response.xpath('//*[@class="detial_txt"]//text()').extract()
        cont = ''.join(cont)
        print(cont)

