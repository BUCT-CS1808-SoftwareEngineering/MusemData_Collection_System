import scrapy
from museum.items import educationItem
import re
# scrapy crawl education15

class Education15Spider(scrapy.Spider):
    name = 'education15'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.njmuseumadmin.com/Classroom/lists']

    def parse(self, response):
        item = educationItem()
        li_list = response.xpath('//*[@id="form"]/div[3]/div[2]/div[@class="Ex_list_dcdiv"]')
        # xp = '/html/body/div[1]/div/div[3]/div/div'
        # num = 1
        for li in li_list:
            name = li.xpath('./a/strong/text()').extract()
            name = ''.join(name)
            print(name)
            img = li.xpath('./div/a/img/@src').extract()
            img = "http://www.njmuseumadmin.com" + ''.join(img)
            print(img)
            cont = "时间/地点：" + li.xpath('./span/text()').extract_first() + li.xpath('./p/text()').extract_first()
            # item['exhibName'] = name
            print(cont)
           
            # item['exhibImg'] = img
            # detail_url = li.xpath('./h5/a/@href').extract_first()
            # detail_url = 'http://www.chnmus.net' + detail_url
            # print(detail_url)
            # # self.deep_urls.append(detail_url)
            # yield scrapy.Request(url=detail_url,callback=self.parse_detail)
            


    
    # def parse_detail(self, response):
    #     img = response.xpath('//*[@id="doZoom"]/p[2]/img/@src').extract()
    #     img = ''.join(img)
    #     img = 'http://www.chnmus.net' + img
    #     print(img)
    #     cont = response.xpath('//*[@id="doZoom"]//text()').extract()
    #     cont = ''.join(cont)
    #     # time = response.xpath('/html/body/div[3]/div[2]/div/ul[2]/li[2]/span[2]/text()').extract()
    #     # time = ''.join(time)
    #     # loca = response.xpath('/html/body/div[3]/div[2]/div/ul[2]/li[2]/span[4]/text()').extract()
    #     # loca = ''.join(loca)
    #     # time = response.xpath('//*[@id="app"]/div/div/div/div/main/div[1]/div[3]/div[2]/div[1]/div[1]/p/text()').extract()
    #     # time = ''.join(time)
    #     # loca = response.xpath('//*[@id="app"]/div/div/div/div/main/div[1]/div[3]/div[2]/div[1]/div[2]/p/text()').extract()
    #     # loca = ''.join(loca)
    #     # cont = cont + '\n展览时间：' + time + '\n展览地点：' + loca
    #     print(cont)
