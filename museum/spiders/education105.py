import scrapy
from museum.items import educationItem

class Education105Spider(scrapy.Spider):
    name = 'education105'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.kzbwg.cn/jy/jiangzuo/']

    def parse_detail(self, response):
        item = response.meta["item"]
        #/html/body/div/div[1]/div[3]/div/div[2]/div[3]/div
        if response.xpath('/html/body/div[6]/div/div/div[2]/p//text()'):
            edu_desc = response.xpath('/html/body/div[6]/div/div/div[2]/p//text()').extract()
            edu_desc = ''.join(edu_desc)
            print(edu_desc)  

    def parse(self, response):
        item = educationItem()
        
        edu_list = response.xpath('/html/body/div[6]/div/div/div[2]/ul/li')
        #//*[@id="thumbnailUL"]
        for li in edu_list:
            #/html/body/div[6]/div/div/div[2]/ul/li[1]/div[1]/div[1]/a
            edu_name = li.xpath('./div[1]/div[1]/a/text()').extract_first()
            print(edu_name)
            #/div[1]/a
            detail_url = 'http://www.kzbwg.cn' + li.xpath('./a/@href').extract_first()
            edu_img = li.xpath('./a/img/@src').extract_first()
            #http://61.187.53.122/
            edu_img = 'http://www.kzbwg.cn' + edu_img
            print(edu_img)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
