import scrapy
from museum.items import exhibitionItem
import re 
# scrapy crawl exhibition33

class Exhibition33Spider(scrapy.Spider):
    name = 'exhibition33'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.tibetanculturemuseum.org/News_List.php?tag=Exhibition']

    def parse(self, response):
        item = exhibitionItem()
        div_list = response.xpath('//*[@id="collection-lb"]/div[1]/ul/li')
        for div in div_list:
            if div.xpath('./div[2]/h3/a/text()').extract_first():
                name = div.xpath('./div[2]/h3/a/text()').extract_first()
                print(name)
                img = div.xpath('./div[1]/a/img/@src').extract_first()
                img = 'http://www.tibetanculturemuseum.org/' + img
                print(img)
                cont = div.xpath('./div[2]/span/a//text()').extract()
                cont = ''.join(cont)
                # cont = div.xpath('./div/div[2]/span/text()').extract_first()
                print(cont)
