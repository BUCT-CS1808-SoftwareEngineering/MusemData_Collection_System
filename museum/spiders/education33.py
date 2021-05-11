import scrapy
from museum.items import educationItem
import re 
# scrapy crawl education33

class Education33Spider(scrapy.Spider):
    name = 'education33'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.tibetanculturemuseum.org/News_List.php?tag=Activity&theId=34']

    def parse(self, response):
        item = educationItem()
        div_list = response.xpath('//*[@id="activity-lb"]/div/ul/li')
        for div in div_list:
            name = div.xpath('./h2/a/text()').extract_first()
            print(name)
            img = div.xpath('./div[1]/a/img/@src').extract_first()
            img = 'http://www.tibetanculturemuseum.org/' + img
            print(img)
            cont = div.xpath('./div[2]//text()').extract()
            cont = ''.join(cont)
            # cont = div.xpath('./div/div[2]/span/text()').extract_first()
            print(cont)
