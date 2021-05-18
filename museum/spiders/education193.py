import scrapy
from museum.items import educationItem
import re 
# scrapy crawl education193

class Education193Spider(scrapy.Spider):
    name = 'education193'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.printingmuseum.cn/Education/NewsList/ZXXYD#comehere']

    def parse(self, response):
        item = educationItem()
        li_list = response.xpath('//*[@id="ulList"]/li')
        num = 1
        for li in li_list:
            if num > 6:
                break
            name = li.xpath('./a/text()').extract_first()
            # name = ''.join(name)
            # name = re.sub('&(.+?);','',name)
            print(name)
            detail_url = "http://www.printingmuseum.cn" + li.xpath('./a/@href').extract_first()
            print(detail_url)
            yield scrapy.Request(url=detail_url,callback=self.parse_detail,meta={'item':item})
    
    def parse_detail(self, response):
        item = response.meta["item"]
        img = response.xpath('//*[@id="divContent"]//img/@src').extract_first()
        # img = 'http://www.njiemuseum.com' + img
        print(img)
        cont = response.xpath('//*[@id="divContent"]//text()').extract()
        cont = ''.join(cont)
        # cont = re.sub('【\d】','',cont)
        print(cont)
