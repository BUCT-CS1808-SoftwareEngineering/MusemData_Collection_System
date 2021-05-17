import scrapy
from museum.items import educationItem
#动态加载
class Education90Spider(scrapy.Spider):
    name = 'education90'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.hbww.org/Views/Activity.aspx?PNo=Education&No=HD&type=List']

    #def parse_detail(self, response):
        #item = response.meta["item"]
        #/html/body/div/div[1]/div[3]/div/div[2]/div[3]/div
        #if response.xpath('/html/body/div/div[1]/div[3]/div/div[2]/div[3]/div/p//text()'):
            #edu_desc = response.xpath('/html/body/div/div[1]/div[3]/div/div[2]/div[3]/div/p//text()').extract()
            #edu_desc = ''.join(edu_desc)
            #print(edu_desc)  

    def parse(self, response):
        item = educationItem()
        
        edu_list = response.xpath('//*[@id="ulActivityList"]/li')
        #//*[@id="thumbnailUL"]
        for li in edu_list:
            #/div[1]/h3
            edu_name = li.xpath('./div[1]/h3/text()').extract_first()
            print(edu_name)
            #/div[1]/a
            #detail_url = 'http://www.ycbwg.com' + li.xpath('./div[1]/a/@href').extract_first()
            #edu_img = li.xpath('./div[1]/a/img/@src').extract_first()
            #http://61.187.53.122/
            #edu_img = 'http://www.ycbwg.com' + edu_img
            #print(edu_img)
            #yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
