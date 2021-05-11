import scrapy
from museum.items import educationItem
#scrapy crawl collection
#scrapy crawl exhiition
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
#scrapy genspider education
class Education9Spider(scrapy.Spider):
    name = 'education134'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.ahgm.org.cn/ahgm/ahgm/kphd/kpzx/index.html']

    def parse(self, response):
        item = educationItem()
        #scrapy crawl education134
        div_list = response.xpath('/html/body/div[6]/div/div/ul[1]/li')
        for li in div_list:
            name = li.xpath('.//a/text()').extract_first()
            print(name)
            detail_url=li.xpath('./a/@href').extract_first()
            detail_url='http://www.ahgm.org.cn'+detail_url
            print(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
    def parse_detail(self, response):
        item = response.meta["item"]
        img = response.xpath('/html/body/div[6]/div/div//img/@src').extract_first()
        if(img):
            img='http://www.ahgm.org.cn'+img
        print(img)
        cont=response.xpath('/html/body/div[6]/div/div//text()').extract()
        cont = ''.join(cont)
        print(cont)