import scrapy
from museum.items import exhibitionItem

class Exhibition113Spider(scrapy.Spider):
    name = 'exhibition113'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.jiawuzhanzheng.org/paper/%e4%ba%b2%e7%88%b1%e7%b2%be%e8%af%9a%e7%88%b1%e5%9b%bd%e6%8a%97%e6%88%98-%e8%af%95%e8%af%84%e8%90%a8%e9%95%87%e5%86%b0%e5%9c%a8%e6%a1%90%e6%a2%93%e6%b5%b7%e6%a0%a1%e7%9a%84%e6%bc%94']

    def parse(self, response):
        item = exhibitionItem()
        exhib_name = response.xpath('/html/body/div[2]/div/div[2]/h1/text()').extract_first()
        print(exhib_name)
        exhib_desc = response.xpath('/html/body/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div[1]//text()').extract()
        exhib_desc = ''.join(exhib_desc)
        print(exhib_desc)
