import scrapy
from museum.items import exhibitionItem
#scrapy crawl collection
#scrapy crawl exhiition
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
#scrapy genspider education
class Education9Spider(scrapy.Spider):
    name = 'exhibition135'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.sz-museum.com/channel/25.html?jbcl_id=14&wd=jbcl']

    def parse(self, response):
        item = exhibitionItem()
        #scrapy crawl exhibition135
        div_list = response.xpath('/html/body/div[1]/div[4]/div/div/div[1]/div[2]/ul/li')
        for li in div_list:
            name = li.xpath('./a/text()').extract_first()
            print(name)
            detail_url=li.xpath('./a/@href').extract_first()
            detail_url='http://www.sz-museum.com'+detail_url
            print(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
    def parse_detail(self, response):
        item = response.meta["item"]
        img = response.xpath('/html/body/div[1]/div[4]/div/div/div[2]/div[2]//img/@src').extract_first()
        print(img)
        cont=response.xpath('/html/body/div[1]/div[4]/div/div/div[2]/div[2]//text()').extract()
        cont = ''.join(cont)
        print(cont)