import scrapy
from museum.items import exhibitionItem
#scrapy crawl collection
#scrapy crawl exhiition
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
#scrapy genspider education
class Education9Spider(scrapy.Spider):
    name = 'exhibition134'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.ahgm.org.cn/ahgm/ahgm/zlzs/cszl/index.html']

    def parse(self, response):
        item = exhibitionItem()
        #scrapy crawl exhibition134
        div_list = response.xpath('/html/body/div[6]/div/div/ul[1]/li')
        for li in div_list:
             name = li.xpath('./div[2]/div[1]/text()').extract_first()
             print(name)
             cont=li.xpath('.//span/text()').extract()
             cont = ''.join(cont)
             print(cont)
             img = li.xpath('./div[1]//img/@src').extract_first()
             if(img):
                img='http://www.ahgm.org.cn'+img
             print(img)
             