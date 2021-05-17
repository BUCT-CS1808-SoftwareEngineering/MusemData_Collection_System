import scrapy
from museum.items import educationItem

class Education114Spider(scrapy.Spider):
    name = 'education114'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.qingzhoumuseum.cn/jy/']

    #/html/body/div[2]/table/tbody/tr[4]/td/table/tbody
    def parse(self, response):
        item = educationItem()
        #1
        edu_name = response.xpath('/html/body/div[2]/table/tbody/tr[4]/td/table/tbody/tr[1]/td/span//text()').extract()
        edu_name = ''.join(edu_name)
        print(edu_name)
        edu_desc = response.xpath('/html/body/div[2]/table/tbody/tr[4]/td/table/tbody/tr[2]/td/span/div/p//text()').extract()
        edu_desc = ''.join(edu_desc)
        print(edu_desc)  
        #2
        edu_name = response.xpath('/html/body/div[2]/table/tbody/tr[4]/td/table/tbody/tr[4]/td/span//text()').extract()
        edu_name = ''.join(edu_name)
        print(edu_name)
        edu_desc = response.xpath('/html/body/div[2]/table/tbody/tr[4]/td/table/tbody/tr[5]/td/span//text()').extract()
        edu_desc = ''.join(edu_desc)
        print(edu_desc)
        #3
        edu_name = response.xpath('/html/body/div[2]/table/tbody/tr[4]/td/table/tbody/tr[8]/td/span//text()').extract()
        edu_name = ''.join(edu_name)
        print(edu_name)
        edu_desc = response.xpath('/html/body/div[2]/table/tbody/tr[4]/td/table/tbody/tr[10]/td/table/tbody/tr[1]/td[1]/a/span//text()').extract()
        edu_desc = ''.join(edu_desc)
        print(edu_desc)
        #4
        edu_name = response.xpath('/html/body/div[2]/table/tbody/tr[4]/td/table/tbody/tr[12]/td/span//text()').extract()
        edu_name = ''.join(edu_name)
        print(edu_name)
        edu_desc = response.xpath('/html/body/div[2]/table/tbody/tr[4]/td/table/tbody/tr[13]/td/span//text()').extract()
        edu_desc = ''.join(edu_desc)
        print(edu_desc)
        #5
        edu_name = response.xpath('/html/body/div[2]/table/tbody/tr[4]/td/table/tbody/tr[16]/td/span//text()').extract()
        edu_name = ''.join(edu_name)
        print(edu_name)
        edu_desc = response.xpath('/html/body/div[2]/table/tbody/tr[4]/td/table/tbody/tr[18]/td/table/tbody/tr[1]/td[1]/a/span//text()').extract()
        edu_desc = ''.join(edu_desc)
        print(edu_desc)
        #6
        edu_name = response.xpath('/html/body/div[2]/table/tbody/tr[4]/td/table/tbody/tr[20]/td/span//text()').extract()
        edu_name = ''.join(edu_name)
        print(edu_name)
        edu_desc = response.xpath('/html/body/div[2]/table/tbody/tr[4]/td/table/tbody/tr[21]/td/span//text()').extract()
        edu_desc = ''.join(edu_desc)
        print(edu_desc)

        