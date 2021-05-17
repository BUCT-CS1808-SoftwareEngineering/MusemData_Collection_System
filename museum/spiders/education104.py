import scrapy
from museum.items import educationItem
#数据解析为空
class Education104Spider(scrapy.Spider):
    name = 'education104'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.tengzhoumuseum.com/newslist/list-4-1.html']

    def parse_detail(self, response):
        item = response.meta["item"]
        
        if response.xpath('/html/body/table[4]/tbody/tr/td[3]/table/tbody/tr[1]/td/table[2]/tbody/tr[4]/td/p[1]/span//text()'):
            edu_desc = response.xpath('/html/body/table[4]/tbody/tr/td[3]/table/tbody/tr[1]/td/table[2]/tbody/tr[4]/td/p[1]/span//text()').extract()
            edu_desc = ''.join(edu_desc)
            print(edu_desc) 
    def parse(self, response):
        item = educationItem()
        #/html/body/table[4]/tbody/tr/td[3]/table/tbody/tr[1]/td/table[2]/tbody/tr[1]/td/table/tbody/tr/td[1]/a
        edu_name = response.xpath('/html/body/table[4]/tbody/tr/td[3]/table/tbody/tr[1]/td/table[2]/tbody/tr[1]/td/table/tbody/tr/td[1]/a/text()').extract_first()
        print(edu_name)
        if response.xpath('/html/body/table[4]/tbody/tr/td[3]/table/tbody/tr[1]/td/table[2]/tbody/tr[1]/td/table/tbody/tr/td[1]/a/@href'):
            detail_url = 'http://www.tengzhoumuseum.com' + response.xpath('/html/body/table[4]/tbody/tr/td[3]/table/tbody/tr[1]/td/table[2]/tbody/tr[1]/td/table/tbody/tr/td[1]/a/@href').extract_first()
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})

