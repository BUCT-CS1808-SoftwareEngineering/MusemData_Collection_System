import scrapy
from museum.items import educationItem

class Education95Spider(scrapy.Spider):
    name = 'education95'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.eywsqsfbwg.com/index.php?m=content&c=index&a=show&catid=9&id=222']

    def parse(self, response):
        item = educationItem()
        
        #edu_list = response.xpath('/html/body/div[2]/div[2]/div')
        
        #for div in edu_list:
        edu_name = response.xpath('/html/body/div[4]/div[2]/div/h2/text()').extract_first() 
        print(edu_name)
        edu_desc = response.xpath('//*[@id="conbox"]//text()').extract()
        edu_desc = ''.join(edu_desc)
        print(edu_desc)            
        edu_img = response.xpath('/html/body/div[4]/div[2]/div/div[1]/div[6]/p/img/@src').extract_first()
        edu_img = 'http://www.eywsqsfbwg.com/' + edu_img
            
        print(edu_img)
