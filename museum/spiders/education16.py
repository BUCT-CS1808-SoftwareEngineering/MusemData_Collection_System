import scrapy
from museum.items import educationItem
import re
# scrapy crawl education16

class Education16Spider(scrapy.Spider):
    name = 'education16'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.tjbwg.com/cn/News.aspx?TypeId=10945']

    def parse(self, response):
        item = educationItem()
        li_list = response.xpath('/html/body/div/div[3]/div/div/div[2]/div[2]/div/div/ul/li')
        for li in li_list:
            name = li.xpath('./a/div[2]/h3/text()').extract()
            name = ''.join(name)
            print(name)
            detail_url = "https://www.tjbwg.com/cn/" + li.xpath('./a/@href').extract_first()
            yield scrapy.Request(url=detail_url,callback=self.parse_detail)
            


    
    def parse_detail(self, response):
        img = 'None'
        if response.xpath('/html/body/div/div[3]/div/div/div[2]/div[2]/div/div[1]/div[2]//img/@src').extract_first():
            img = response.xpath('/html/body/div/div[3]/div/div/div[2]/div[2]/div/div[1]/div[2]//img/@src').extract_first()
            img = 'https://www.tjbwg.com' + img
        print(img)
        cont = response.xpath('/html/body/div/div[3]/div/div/div[2]/div[2]/div/div[1]/div[2]//text()').extract()
        cont = ''.join(cont)
        cont = re.sub('\s','',cont)
        time = response.xpath('/html/body/div/div[3]/div/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/text()').extract()
        time = ''.join(time)
        time = re.sub('\s','',time)
        cont = cont + '\n时间：' + time 
        print(cont)
