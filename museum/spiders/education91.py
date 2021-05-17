import scrapy
from museum.items import educationItem

class Education91Spider(scrapy.Spider):
    name = 'education91'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.pdsm.org.cn/front/information/index/cat_id/15/pid/8.html?page=1']
    url = 'http://www.pdsm.org.cn/front/information/index/cat_id/15/pid/8.html?page=%d'
    page_num = 2
    def parse_detail(self, response):
        item = response.meta["item"]
        #详情页描述信息位置大多不同-故爬取一个
        #/html/body/div[3]/div[4]/section[1]
        #/html/body/div[3]/div[4]/section[1]/section/section[1]
        #/html/body/div[3]/div[4]/section[1]/section
        #/html/body/div[3]/div[4]/section[1]/section
        #/html/body/div[3]/div[4]/section[1]/section/section/section/section/section
        if response.xpath('/html/body/div[3]/div[4]/section[1]/p//text()'):
            edu_desc = response.xpath('/html/body/div[3]/div[4]/section[1]/p//text()').extract()
            edu_desc = ''.join(edu_desc)
            print(edu_desc)  

    def parse(self, response):
        item = educationItem()
        
        edu_list = response.xpath('/html/body/div[3]/div[3]/ul/li')
        
        for li in edu_list:
            #/div[2]/a
            edu_name = li.xpath('./div[2]/a/text()').extract_first()
            print(edu_name)
            #/div[2]/a
            detail_url = 'http://www.pdsm.org.cn' + li.xpath('./div[2]/a/@href').extract_first()
            #图像无法爬取
            #edu_img = li.xpath('./div[1]/a/img/@src').extract_first()
            #edu_img = 'http://www.ycbwg.com' + edu_img
            #print(edu_img)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        if self.page_num <= 4:
            new_url = (self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)

