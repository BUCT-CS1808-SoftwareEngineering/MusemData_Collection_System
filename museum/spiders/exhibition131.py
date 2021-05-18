import scrapy
from museum.items import exhibitionItem 
#scrapy crawl collection
#scrapy crawl exhiition
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
#scrapy genspider education
class Education9Spider(scrapy.Spider):
    name = 'exhibition131'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.mtybwg.org.cn/zhanlan/105-1.aspx']

    def parse(self, response):
        item = educationItem()
        #scrapy crawl exhibition131
        div_list = response.xpath('//*[@id="container"]/li')
        for li in div_list:
             name = li.xpath('.//img/@alt').extract_first()
             print(name)
             img=li.xpath('.//img/@src').extract_first()
             img='http://www.mtybwg.org.cn'+img
             print(img)
             detail_url=li.xpath('.//a/@href').extract_first()
             detail_url='http://www.mtybwg.org.cn'+detail_url
             print(detail_url)
             yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
    def parse_detail(self, response):
        item = response.meta["item"]
        #img = response.xpath('//*[@class="nr"]//img/@src').extract_first()
        #print(img)
        cont=response.xpath('//*[@class="detailcon"]//text()').extract()
        cont = ''.join(cont)
        print(cont)