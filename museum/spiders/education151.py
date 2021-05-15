import scrapy
from museum.items import educationItem
#scrapy crawl collection
#scrapy crawl exhiition
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
#scrapy genspider education
class Education9Spider(scrapy.Spider):
    name = 'education151'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.zj-museum.com.cn/zjbwg/zjbwg/gw/dj/index.html']

    def parse(self, response):
        item = educationItem()
        #scrapy crawl education151
        div_list = response.xpath('/html/body/div[3]/div[2]/ul[2]/li')
        for li in div_list:
            name = li.xpath('./a/text()').extract_first()
            print(name)
            detail_url=li.xpath('./a/@href').extract_first()
            detail_url='http://www.zj-museum.com.cn'+detail_url
            print(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
    def parse_detail(self, response):
        item = response.meta["item"]
        img = response.xpath('//*[@class="la-info"]//img/@src').extract_first()
        if(img):
            img='http://www.zj-museum.com.cn'+img
        print(img)
        cont=response.xpath('//*[@class="la-info"]//text()').extract()
        cont = ''.join(cont)
        print(cont)