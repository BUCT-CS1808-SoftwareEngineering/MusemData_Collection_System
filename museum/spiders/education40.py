import scrapy
from museum.items import educationItem
from selenium import webdriver
import re 
import json
# scrapy crawl education40

class Education40Spider(scrapy.Spider):
    name = 'education40'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://bpmuseum.com/index.php?m=content&c=index&a=lists&catid=26']
    new_urls = ['https://bpmuseum.com/index.php?m=content&c=index&a=lists&catid=26']
    deep_urls = []

    def __init__(self):
        self.bro = webdriver.Firefox()
        # self.brom = webdriver.Firefox()

    def parse(self, response):
        item = educationItem()
        li_list = response.xpath('//*[@id="mm-0"]/div[4]/div/div/div[2]/div/ul/li')
        # li1 = response.xpath('/html/body/div[1]')
        # print(li1)
        num = 1
        for li in li_list:
            if num > 6:
                break
            name = li.xpath('./div[2]/h3/a/text()').extract_first()
            print(name)
            img = li.xpath('./div[1]/a/img/@src').extract_first()
            if img[0] == '/':
                img = "https://bpmuseum.com" + img
            print(img)
            cont = li.xpath('./div[2]/p/text()').extract_first()
            cont = "时间：" + li.xpath('./div[2]/span/text()').extract_first() + "\n" + cont
            print(cont)
            detail_url = "https://bpmuseum.com" + li.xpath('./div[1]/a/@href').extract_first()
            # print(detail_url)
            # yield scrapy.Request(url=detail_url,callback=self.parse_detail,meta={'item':item})
    
    # def parse_detail(self, response):
    #     item = response.meta["item"]
    #     img = "http://www.yagmjng.com" + response.xpath('//*[@id="zcnr"]/p//img/@src').extract_first()
    #     print(img)
    #     cont = response.xpath('//*[@id="zcnr"]/p//text()').extract()
    #     cont = ''.join(cont)
    #     # cont = re.sub('【\d】','',cont)
    #     print(cont)
    def closed(self,spider):
        self.bro.quit()
        # self.brom.quit()
