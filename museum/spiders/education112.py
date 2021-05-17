import scrapy
from museum.items import educationItem
#详情页无数据解析
class Education112Spider(scrapy.Spider):
    name = 'education112'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://museum.linyi.cn/sjzc.htm']

    def parse_detail(self, response):
        item = response.meta["item"]
        #/html/body/div[3]/div[3]/div[2]/p[17]/img
        if response.xpath('/html/body/div[3]/div/div[2]/form/table/tbody/tr[4]/td/div/div/div/p[1]/img/@src'):
            edu_img = response.xpath('/html/body/div[3]/div/div[2]/form/table/tbody/tr[4]/td/div/div/div/p[1]/img/@src').extract_first()
            edu_img = 'http://museum.linyi.cn' + edu_img
            print(edu_img)
        if response.xpath('/html/body/div[3]/div/div[2]/form/table/tbody/tr[4]/td/div/div/div/p[2]//text()'):
            edu_desc = response.xpath('/html/body/div[3]/div/div[2]/form/table/tbody/tr[4]/td/div/div/div/p[2]//text()').extract()
            edu_desc = ''.join(edu_desc)
            print(edu_desc)  
        #print("1")

    def parse(self, response):
        item = educationItem()
        
        edu_list = response.xpath('/html/body/div[3]/div/div[2]/ul/li')
        for div in edu_list:
            edu_name = div.xpath('./a/text()').extract_first()
            print(edu_name)
            
            detail_url = div.xpath('./a/@href').extract_first()
            detail_url = 'http://museum.linyi.cn/' + detail_url
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
