import scrapy
from museum.items import educationItem
#scrapy crawl collection
#scrapy crawl exhiition
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
#scrapy genspider education
class Education9Spider(scrapy.Spider):
    name = 'education143'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.teamuseum.cn/news/classroom.htm']

    def parse(self, response):
        item = educationItem()
        #scrapy crawl education143
        div_list = response.xpath('/html/body/div[4]/ul/li')
        for li in div_list:
            name = li.xpath('.//h2/text()').extract_first()
            print(name)
            img = li.xpath('.//img/@src').extract_first()
            #img='http://www.ahgm.org.cn'+img
            print(img)
            cont=li.xpath('.//li/text()').extract()
            cont = ''.join(cont)
            print(cont)