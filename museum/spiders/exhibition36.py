import scrapy
from museum.items import exhibitionItem 
import re
import json
from selenium import webdriver
# scrapy crawl exhibition36

class Exhibition36Spider(scrapy.Spider):
    name = 'exhibition36'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.tssbwg.com.cn/index.php?m=content&c=index&a=lists&catid=30']

    new_urls = ['http://www.tssbwg.com.cn/index.php?m=content&c=index&a=lists&catid=30']
    deep_urls = []

    def __init__(self):
        self.bro = webdriver.Firefox()
        self.brom = webdriver.Firefox()

    def parse(self, response):
        item = exhibitionItem()
        div_list = response.xpath('/html/body/table[2]/tbody/tr/td/table[2]/tbody/tr/td[3]/table[2]/tbody/tr/td/table')
        # print(div_list)
        num = 1
        for div in div_list:
            if div.xpath('./tbody/tr/td[2]/a/@href').extract_first():
                if num > 6:
                    break
                num += 1
                detail_url = div.xpath('./tbody/tr/td[2]/a/@href').extract_first()
                # detail_url = "http://www.sxgm.org" + detail_url
                self.deep_urls.append(detail_url)
                yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        
    
    def parse_detail(self, response):
        item = response.meta["item"]
        exhib_name = response.xpath('/html/body/table[2]/tbody/tr/td/div/table[3]/tbody/tr/td/div/text()').extract_first()
        print(exhib_name)
        img = response.xpath('/html/body/table[2]/tbody/tr/td/div/table[6]/tbody/tr/td//img/@src').extract_first()
        # img = 'http://www.sxgm.org' + img
        print(img)
        cont = response.xpath('/html/body/table[2]/tbody/tr/td/div/table[6]/tbody/tr/td//text()').extract()
        cont = ''.join(cont)
        # cont = re.sub('【\d】','',cont)
        print(cont)

    def closed(self,spider):
        self.bro.quit()
        self.brom.quit()
