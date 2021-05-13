import scrapy
from museum.items import educationItem
#scrapy crawl collection
#scrapy crawl exhiition
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
#scrapy genspider education
class Education9Spider(scrapy.Spider):
    name = 'education147'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.nbmuseum.cn/col/col881/index.html']

    def parse(self, response):
        item = educationItem()
        #scrapy crawl education147
        div_list = response.xpath('/html/body/div[3]/div[2]/div[2]/div/div/li')
        for li in div_list:
            name = li.xpath('.//a/text()').extract_first()
            print(name)
            