import scrapy
from museum.items import educationItem
#scrapy crawl collection
#scrapy crawl exhiition
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
#scrapy genspider education
class Education9Spider(scrapy.Spider):
    name = 'education124'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.rjjng.com.cn/jiaoyu.thtml?id=10979']

    def parse(self, response):
        item = educationItem()
        #scrapy crawl education124
        _list = response.xpath('/html/body/div[1]/div[3]/div/div[2]/ul/li')
        for li in _list:
            name = li.xpath('./a/text()').extract_first()
            print(name)
            detail_url = li.xpath('./a/@href').extract_first()
            #detail_url = 'http://www.zgtcbwg.com' + detail_url
            print(detail_url)
            yield scrapy.Request(url=detail_url,callback=self.parse_detail)
    def parse_detail(self, response):
        img = response.xpath('//*[@class="nr"]//img/@src').extract_first()
        print(img)
        cont=response.xpath('//*[@class="nr"]//text()').extract()
        cont = ''.join(cont)
        print(cont)