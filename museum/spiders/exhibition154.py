import scrapy
from museum.items import educationItem
#scrapy crawl collection
#scrapy crawl exhiition
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
#scrapy genspider education
class Education9Spider(scrapy.Spider):
    name = 'exhibition154'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.wxmuseum.com/Exhibition/Index/BaseDisplay']

    def parse(self, response):
        item = educationItem()
        #scrapy crawl exhibition154
        div_list = response.xpath('/html/body/div[5]/div/div/div/div[2]/ul[2]/li')
        for li in div_list:
            name = li.xpath('.//h2/text()').extract_first()
            name=str.strip(name)
            print(name)
            img=li.xpath('.//img/@src').extract_first()
            #img='http://www.qzhjg.cn'+img
            print(img)
            detail_url=li.xpath('.//a/@href').extract_first()
            detail_url='http://www.wxmuseum.com'+detail_url
            print(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
    def parse_detail(self, response):
        item = response.meta["item"]
        cont=response.xpath('//*[@class="detailcont"]//text()').extract()
        cont = ''.join(cont)
        print(cont)