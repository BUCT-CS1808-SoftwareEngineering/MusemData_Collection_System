import scrapy
from museum.items import educationItem
#scrapy crawl collection
#scrapy crawl exhiition
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
#scrapy genspider education
class Education9Spider(scrapy.Spider):
    name = 'education156'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.ntmuseum.com/colunm2/']

    def parse(self, response):
        item = educationItem()
        #scrapy crawl education156
        div_list = response.xpath('/html/body/section[2]/div[3]/div[1]/div[3]/ul/li[1]/div[2]/p[1]')
        print(div_list)