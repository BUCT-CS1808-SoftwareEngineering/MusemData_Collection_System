import scrapy
from museum.items import educationItem
#scrapy crawl collection
#scrapy crawl exhiition
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
#scrapy genspider education
class Education9Spider(scrapy.Spider):
    name = 'exhibition136'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.hzwhbwg.com/index.php/list-11-1.html']

    def parse(self, response):
        item = educationItem()
        #scrapy crawl exhibition136
        div_list = response.xpath('/html/body/div[6]/div[2]/ul/li')
        for li in div_list:
            name = li.xpath('.//h5/text()').extract_first()
            print(name)
            img=li.xpath('.//img/@src').extract_first()
            img='http://www.hzwhbwg.com'+img
            print(img)
            detail_url=li.xpath('.//a/@href').extract_first()
            detail_url='http://www.hzwhbwg.com'+detail_url
            print(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
    def parse_detail(self, response):
        item = response.meta["item"]
        #img = response.xpath('//*[@class="nr"]//img/@src').extract_first()
        #print(img)
        cont=response.xpath('//*[@class="newscontent"]//text()').extract()
        cont = ''.join(cont)
        print(cont)