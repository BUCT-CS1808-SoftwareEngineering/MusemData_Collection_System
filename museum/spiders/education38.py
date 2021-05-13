import scrapy
from museum.items import educationItem
import re 
import json
# scrapy crawl education38

class Education38Spider(scrapy.Spider):
    name = 'education38'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.dtxsmuseum.com/news_title_list.aspx?category_id=31']

    def parse(self, response):
        item = educationItem()
        li_list = response.xpath('//*[@id="form1"]/div[4]/div[2]/ul/li')
        num = 1
        for li in li_list:
            if num > 6:
                break
            name = li.xpath('./a/text()').extract_first()
            print(name)
            detail_url = "http://www.dtxsmuseum.com" + li.xpath('./a/@href').extract_first()
            print(detail_url)
            yield scrapy.Request(url=detail_url,callback=self.parse_detail,meta={'item':item})
    
    def parse_detail(self, response):
        item = response.meta["item"]
        img = "http://www.dtxsmuseum.com" + response.xpath('//*[@id="form1"]/div[4]/div[2]/div[4]//img/@src').extract_first()
        # img = 'http://www.njiemuseum.com' + img
        print(img)
        cont = response.xpath('//*[@id="form1"]/div[4]/div[2]/div[4]//text()').extract()
        cont = ''.join(cont)
        # cont = re.sub('【\d】','',cont)
        print(cont)

