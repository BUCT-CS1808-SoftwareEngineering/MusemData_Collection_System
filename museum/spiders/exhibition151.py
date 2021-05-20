import scrapy
from museum.items import exhibitionItem
#scrapy crawl collection
#scrapy crawl exhiition
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
#scrapy genspider education
class Education9Spider(scrapy.Spider):
    name = 'exhibition151'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.zj-museum.com.cn/zjbwg/zjbwg/zs/ztzl/index.html']

    def parse(self, response):
        item = exhibitionItem()
        #scrapy crawl exhibition151
        div_list = response.xpath('//*[@class="qtitemwp"]')
        for li in div_list:
            name = li.xpath('.//*[@class="qtitem-tt"]/text()').extract_first()
            print(name)
            img=li.xpath('.//img/@src').extract_first()
            img='http://www.zj-museum.com.cn'+img
            print(img)
            detail_url=li.xpath('./a/@href').extract_first()
            detail_url='http://www.zj-museum.com.cn'+detail_url
            print(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
    def parse_detail(self, response):
        item = response.meta["item"]
        #img = response.xpath('//*[@class="nr"]//img/@src').extract_first()
        #print(img)
        cont=response.xpath('/html/body/div[3]/div[2]/div//text()').extract()
        cont = ''.join(cont)
        print(cont)