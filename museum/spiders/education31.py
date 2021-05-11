import scrapy
from museum.items import educationItem
import re 
# scrapy crawl education31

class Education31Spider(scrapy.Spider):
    name = 'education31'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.nxgybwg.com/e/action/ListInfo/?classid=45']

    def parse(self, response):
        item = educationItem()
        li_list = response.xpath('//*[@id="body_wrap"]/div/div[2]/div[2]/div[2]/dl')
        num = 1
        for li in li_list:
            if num > 6:
                break
            name = li.xpath('./dt/a/text()').extract_first()
            # name = ''.join(name)
            # name = re.sub('&(.+?);','',name)
            print(name)
            # item['exhibName'] = name          
            # item['exhibImg'] = img
            # //*[@id="body_wrap"]/div/div[2]/div[2]/div[2]/dl[1]/
            img = li.xpath('./dd[1]/a/img/@src').extract_first()
            # img = 'http://www.njiemuseum.com' + img
            print(img)
            detail_url = "http://www.nxgybwg.com" + li.xpath('./dt/a/@href').extract_first()
            print(detail_url)
            # //*[@id="body_wrap"]/div/div[2]/div[2]/div[2]/dl[1]/
            cont = li.xpath('./dt/span/text()').extract_first()
            print(cont)
            # yield scrapy.Request(url=detail_url,callback=self.parse_detail,meta={'item':item})
    
    # def parse_detail(self, response):
    #     item = response.meta["item"]
    #     cont = response.xpath('//*[@id="ContentPlaceHolder1_cnt"]/div/div/div[5]//text()').extract()
    #     cont = ''.join(cont)
    #     # cont = re.sub('【\d】','',cont)
    #     print(cont)

