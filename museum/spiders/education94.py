import scrapy
from museum.items import educationItem

class Education94Spider(scrapy.Spider):
    name = 'education94'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.kfsbwg.com/html/huodong/']

    def parse(self, response):
        item = educationItem()
        
        edu_list = response.xpath('/html/body/div[2]/div[2]/div')
        #/html/body/div[2]/div[2]/div
        for div in edu_list:
            #/html/body/div[2]/div[2]/div[1]/p
            edu_desc = div.xpath('./p//text()').extract()
            edu_desc = ''.join(edu_desc)
            print(edu_desc)
            #/html/body/div[2]/div[2]/div[1]/a/img
            edu_img = div.xpath('./a/img/@src').extract_first()
            #edu_img = 'http://www.ycbwg.com' + edu_img
            print(edu_img)

            #edu_desc = div.xpath('//html/body/div/div[4]/div[2]/div/div[2]/p//text()').extract()
            #edu_desc = ''.join(edu_desc)
            #print(edu_desc)
