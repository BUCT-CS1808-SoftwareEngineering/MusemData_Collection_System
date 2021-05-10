import scrapy
from museum.items import exhibitionItem
import re 
# scrapy crawl exhibition23

class Exhibition23Spider(scrapy.Spider):
    name = 'exhibition23'
    start_urls = ['http://www.nanhaimuseum.org/411899/418245/index1.html']
    url = 'http://www.nanhaimuseum.org/411899/418245/index%d.html'
    page_num = 2

    def parse(self, response):
        item = exhibitionItem()
        div_list = response.xpath('//*[@id="tiles"]/li')
        for div in div_list:
            exhib_name = div.xpath('./p/a//text()').extract_first()
            print(exhib_name)
            img = div.xpath('./a/img/@src').extract_first()
            img = 'http://www.nanhaimuseum.org' + img
            print(img)
            detail_url = div.xpath('./a/@href').extract_first()
            detail_url = detail_url
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        
        if self.page_num <= 2:
            new_url = (self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)
    
    def parse_detail(self, response):
        item = response.meta["item"]
        cont = response.xpath('/html/body/div/div[2]/div[1]/div[2]/div[4]//text()').extract()
        cont = ''.join(cont)
        cont = re.sub('【\d】','',cont)
        print(cont)
        # yield item
