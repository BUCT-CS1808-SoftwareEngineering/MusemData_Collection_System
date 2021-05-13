import scrapy
from museum.items import educationItem
#scrapy crawl collection
#scrapy crawl exhiition
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
#scrapy genspider education
class Education9Spider(scrapy.Spider):
    name = 'exhibition138'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.ahm.cn/Exhibition/TListNow/xztj']

    def parse(self, response):
        item = educationItem()
        #scrapy crawl exhibition138
        div_list = response.xpath('//*[@id="zltj"]/li')
        for li in div_list:
            name = li.xpath('.//h3/text()').extract_first()
            print(name)
            img = li.xpath('.//img/@src').extract_first()
            print(img)
            detail_url=li.xpath('.//@href').extract_first()
            #detail_url='http://www.qzhjg.cn'+detail_url
            if(detail_url.find("qmxk")<0):
                detail_url=detail_url.replace("index","jian")
            else:
                detail_url=detail_url.replace("index","zljj")
            print(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
    def parse_detail(self, response):
        item = response.meta["item"]
        #img = response.xpath('//*[@class="nr"]//img/@src').extract_first()
        #print(img)
        cont=response.xpath('//*[@class="cont"]//text()').extract()
        cont = ''.join(cont)
        print(cont)