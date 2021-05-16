import scrapy
from museum.items import educationItem
#scrapy crawl collection
#scrapy crawl exhiition
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
#scrapy genspider education
class Education9Spider(scrapy.Spider):
    name = 'exhibition159'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.slmmm.com/exhibit/basic.html']

    def parse(self, response):
        item = educationItem()
        #scrapy crawl exhibition159
        div_list = response.xpath('//*[@class="row thumbnail-content"]')
        for li in div_list:
            name = li.xpath('.//h2/text()').extract_first()
            print(name)
            img=li.xpath('.//img/@src').extract_first()
            img='https://www.slmmm.com'+img
            print(img)
            cont=li.xpath('.//*[@class="thumbnail-text-panel-text"]//text()').extract()
            cont = ''.join(cont)
            print(cont)