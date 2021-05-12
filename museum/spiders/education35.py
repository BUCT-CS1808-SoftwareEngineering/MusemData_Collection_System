import scrapy
from museum.items import educationItem
import re 
import json
# scrapy crawl education35

class Education35Spider(scrapy.Spider):
    name = 'education35'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.plsbwg.com/index.php?m=content&c=index&a=lists&catid=49']

    def parse(self, response):
        item = educationItem()
        li_list = response.xpath('/html/body/div[3]/div/div[2]/div[2]/ul/li')
        num = 1
        for li in li_list:
            if num > 6:
                break
            name = li.xpath('./a/div[2]/h3/text()').extract_first()
            print(name)
            img = li.xpath('./a/div[1]/img/@src').extract_first()
            # img = 'http://www.njiemuseum.com' + img
            print(img)
            cont = "时间：" + li.xpath('a/div[3]/i/text()').extract_first() + '-' + li.xpath('a/div[3]/span/text()').extract_first()
            print(cont)
            # detail_url = li.xpath('./a/@href').extract_first()
            # print(detail_url)
            # yield scrapy.Request(url=detail_url,callback=self.parse_detail,meta={'item':item})
    
    # def parse_detail(self, response):
    #     item = response.meta["item"]
    #     cont = response.xpath('//*[@id="ContentPlaceHolder1_cnt"]/div/div/div[5]//text()').extract()
    #     cont = ''.join(cont)
    #     # cont = re.sub('【\d】','',cont)
    #     print(cont)

