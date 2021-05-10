import scrapy
from museum.items import exhibitionItem
import re 
from selenium import webdriver
# scrapy crawl exhibition24



class Exhibition24Spider(scrapy.Spider):
    name = 'exhibition24'
    start_urls = ['http://www.sxgm.org/home/picnews/index/c_id/94/lanmu/59.html',
    'http://www.sxgm.org/home/picnews/index/c_id/95/lanmu/59.html',
    'http://www.sxgm.org/home/picnews/index/c_id/109/lanmu/59.html']

    new_urls = ['http://www.sxgm.org/home/picnews/index/c_id/94/lanmu/59.html',
    'http://www.sxgm.org/home/picnews/index/c_id/95/lanmu/59.html',
    'http://www.sxgm.org/home/picnews/index/c_id/109/lanmu/59.html']
    deep_urls = []

    def __init__(self):
        self.bro = webdriver.Firefox()
        self.brom = webdriver.Firefox()

    def parse(self, response):
        item = exhibitionItem()
        div_list = response.xpath('/html/body/div[5]/div/div[2]/ul/li')
        # print(div_list)
        for div in div_list:
            detail_url = div.xpath('./a/@href').extract_first()
            detail_url = "http://www.sxgm.org" + detail_url
            self.deep_urls.append(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        
    
    def parse_detail(self, response):
        item = response.meta["item"]
        exhib_name = response.xpath('/html/body/div[5]/div/div[2]/div[4]/table/tbody/tr[1]/td[2]/font/text()').extract_first()
        print(exhib_name)
        img = response.xpath('/html/body/div[5]/div/div[2]/div[4]/table/tbody/tr[1]/td[1]/div/div[1]//img/@src').extract_first()
        img = 'http://www.sxgm.org' + img
        # img = 
        print(img)
        cont = response.xpath('/html/body/div[5]/div/div[2]/div[4]/table/tbody/tr[2]/td/div//text()').extract()
        cont = ''.join(cont)
        # cont = re.sub('【\d】','',cont)
        print(cont)

    def closed(self,spider):
        self.bro.quit()
        self.brom.quit()