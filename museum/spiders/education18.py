import scrapy
from museum.items import educationItem 
import re
import json
# scrapy crawl education18

class Education18Spider(scrapy.Spider):
    name = 'education18'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.pgm.org.cn/pgm/wfdjt/list.shtml']

    def parse_detail(self, response):
        item = response.meta["item"]
        url = response.meta["url"]
        cont = 'None'
        if response.xpath('//*[@id="content"]//text()').extract():
            cont = response.xpath('//*[@id="content"]//text()').extract()
            cont = ''.join(cont)
        img = "None"
        if response.xpath('//*[@id="content"]//img/@src').extract_first():
            img = response.xpath('//*[@id="content"]//img/@src').extract_first()
            img = url + img
        print(img)
        # cont = cont + des
        # cont = re.sub('&(.+?);','',cont)
        print(cont)
       
        # yield item


    def parse(self, response):
        item = educationItem()
        div_list = response.xpath('/html/body/div/div[3]/div[2]/ul/li')
        for div in div_list:
            # img = div.xpath('./div/a/div[1]/img/@src').extract_first()
            # img = "https://www.tjbwg.com" + img
            # print(img)
            name = div.xpath('./a/text()').extract_first()
            print(name)
            detail_url = div.xpath('./a/@href').extract_first()
            detail_url = detail_url.replace(".",'',4)
            detail_url = detail_url.replace("/",'',1)
            detail_url = "http://www.pgm.org.cn" + detail_url
            print(detail_url)
            url = re.search('(.+?[0-9]+)/',detail_url).group()
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item,'url':url})
