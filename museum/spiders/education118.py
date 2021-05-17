import scrapy
from museum.items import educationItem
#空
class Education118Spider(scrapy.Spider):
    name = 'education118'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.lushanmuseum.com/xsyd_info.asp?id=383']

    def parse(self, response):
        item = educationItem()
        
        #edu_list = response.xpath('/html/body/div[2]/div[2]/div')
        
        #for div in edu_list:
        edu_name = response.xpath('/html/body/table[4]/tbody/tr/td[3]/table/tbody/tr[4]/td/div[1]/text()').extract_first() 
        print(edu_name)
        edu_desc = response.xpath('/html/body/table[4]/tbody/tr/td[3]/table/tbody/tr[4]/td/div[4]//text()').extract()
        edu_desc = ''.join(edu_desc)
        print(edu_desc)            
        

