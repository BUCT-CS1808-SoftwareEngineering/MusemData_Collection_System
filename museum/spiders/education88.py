import scrapy
from museum.items import educationItem
#由于页面动态加载，只能列举一个教育活动
class Education88Spider(scrapy.Spider):
    name = 'education88'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://jzmsm.org/yk/huodong1/2021-04-02/1790.html']

    

    def parse(self, response):
        item = educationItem()
        
        edu_name = response.xpath('/html/body/div[6]/div/div[1]/center/h1/text()').extract_first()
        print(edu_name)
        edu_desc = response.xpath('/html/body/div[6]/div/div[3]/p//text()').extract()
        edu_desc = ''.join(edu_desc)
        print(edu_desc)  
        edu_img = response.xpath('/html/body/div[6]/div/div[3]/p[7]/img/@src').extract_first()
        edu_img = 'http://jzmsm.org' + edu_img
        print(edu_img)
            
