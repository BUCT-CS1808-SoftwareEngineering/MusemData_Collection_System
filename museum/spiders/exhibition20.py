import scrapy
from museum.items import exhibitionItem 
# scrapy crawl exhibition20

class Exhibition20Spider(scrapy.Spider):
    name = 'exhibition20'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.gansumuseum.com/zl/list-55.html']

    def parse(self, response):
        item = exhibitionItem()
        div_list = response.xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/ul/li')
        for div in div_list:
            exhib_name = div.xpath('./div/div/div[1]/label/text()').extract_first()
            print(exhib_name)
            img = 'http://www.gansumuseum.com' + div.xpath('./div/a/img/@src').extract_first()
            cont = div.xpath('./div/div/div[2]/p/text()').extract_first()
            print(img)
            print(cont)
            # yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})

