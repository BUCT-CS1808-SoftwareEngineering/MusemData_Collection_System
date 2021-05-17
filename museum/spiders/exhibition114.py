import scrapy
from museum.items import exhibitionItem
#需要url的图片和详情页源代码中多了一个"."所以无法进行数据解析
class Exhibition114Spider(scrapy.Spider):
    name = 'exhibition114'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.qingzhoumuseum.cn/zl/']

    def parse(self, response):
        item = exhibitionItem()
       
        exhib_list = response.xpath('/html/body/div[2]/table/tbody/tr[3]/td/table/tbody/tr')
        
        for li in exhib_list:
            #/html/body/div[2]/table/tbody/tr[3]/td/table[1]/tbody/tr[1]/td[2]/a/span
            exhib_name = li.xpath('./td[2]/a/span/text()').extract_first()
            print(exhib_name)
