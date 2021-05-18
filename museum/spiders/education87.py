import scrapy
from museum.items import educationItem

class Education87Spider(scrapy.Spider):
    name = 'education87'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.ycbwg.com/web/education/socialEducation/list.shtml']

    def parse_detail(self, response):
        item = response.meta["item"]
        if response.xpath('/html/body/div/div[1]/div[3]/div/div[2]/div[3]/div/p//text()'):
            edu_desc = response.xpath('/html/body/div/div[1]/div[3]/div/div[2]/div[3]/div/p//text()').extract()
            edu_desc = ''.join(edu_desc)
            print(edu_desc)  

    def parse(self, response):
        item = educationItem()
        
        edu_list = response.xpath('/html/body/div/div[1]/div[3]/div/div[2]/div[3]/div[1]/ul/li')
        #//*[@id="thumbnailUL"]
        for li in edu_list:
            #/div[2]/h1/a
            edu_name = li.xpath('./div[2]/h1/a/text()').extract_first()
            print(edu_name)
            #/div[1]/a
            detail_url = 'http://www.ycbwg.com' + li.xpath('./div[1]/a/@href').extract_first()
            edu_img = li.xpath('./div[1]/a/img/@src').extract_first()
            #http://61.187.53.122/
            edu_img = 'http://www.ycbwg.com' + edu_img
            print(edu_img)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
