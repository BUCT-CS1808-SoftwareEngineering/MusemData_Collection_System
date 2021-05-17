import scrapy
from museum.items import exhibitionItem
#解析数据为空
class Exhibition104Spider(scrapy.Spider):
    name = 'exhibition104'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.tengzhoumuseum.com/product/570.html']

    def parse(self, response):
        item = exhibitionItem()
        exhib_name = response.xpath('/html/body/table[4]/tbody/tr/td[2]/table/tbody/tr[1]/td/table[2]/tbody/tr[1]/td/text()').extract_first()
        print(exhib_name)
        #exhib_desc = response.xpath('/html/body/table[4]/tbody/tr/td[2]/table/tbody/tr[1]/td/table[2]/tbody/tr[3]/td/p/span//text()').extract()
        #exhib_desc = ''.join(exhib_desc)
        #print(exhib_desc)
        #exhib_img = response.xpath('/html/body/table[4]/tbody/tr/td[2]/table/tbody/tr[1]/td/table[2]/tbody/tr[3]/td/p[5]/span/span/img/@src').extract_first()
            
        #exhib_img = 'http://www.tengzhoumuseum.com' + exhib_img
        #print(exhib_img)
