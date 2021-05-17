import scrapy
from museum.items import educationItem
#输出为空
class Education116Spider(scrapy.Spider):
    name = 'education116'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.gzsbwg.cn/html/infolist-14-1.html']

    def parse(self, response):
        item = educationItem()
        
        
        edu_name ='常设展览'
        print(edu_name)
        edu_img = response.xpath('/html/body/div[5]/div/div[1]/div/div/p[4]/img/@src').extract_first()
        edu_img = 'http://www.gzsbwg.cn' + edu_img    
        edu_desc = response.xpath('/html/body/div[5]/div/div[1]/div/div/text()').extract()
        edu_desc = ''.join(edu_desc)
        print(edu_desc)
        
