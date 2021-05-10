import scrapy
from museum.items import educationItem
import re 
# scrapy crawl education23

class Education23Spider(scrapy.Spider):
    name = 'education23'
    start_urls = ['http://www.nanhaimuseum.org/411906/419341/index1.html']

    def parse(self, response):
        item = educationItem()
        li_list = response.xpath('/html/body/div/div[2]/div/div[2]/ul/a')
        for li in li_list:
            # item['exhibName'] = name          
            # item['exhibImg'] = img
            img = li.xpath('./img/@src').extract_first()
            img = 'http://www.nanhaimuseum.org' + img
            print(img)
            detail_url = li.xpath('./@href').extract_first()
            # print(detail_url)
            yield scrapy.Request(url=detail_url,callback=self.parse_detail,meta={'item':item})
    
    def parse_detail(self, response):
        item = response.meta["item"]
        name = response.xpath('/html/body/div/div[2]/div[1]/div[2]/h1/text()').extract()
        name = ''.join(name)
        name = re.sub('&(.+?);','',name)
        print(name)
        cont = response.xpath('/html/body/div/div[2]/div[1]/div[2]/div[4]//text()').extract()
        cont = ''.join(cont)
        cont = re.sub('【\d】','',cont)
        print(cont)
