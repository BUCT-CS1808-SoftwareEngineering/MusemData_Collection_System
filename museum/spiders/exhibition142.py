import scrapy
from museum.items import educationItem
#scrapy crawl collection
#scrapy crawl exhiition
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
#scrapy genspider education
class Education9Spider(scrapy.Spider):
    name = 'exhibition142'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.nanhujng.com/clzl/jbcl/']
    i=1
    def parse(self, response):
        item = educationItem()
        #scrapy crawl exhibition142
        div_list = response.xpath('/html/body/div[6]/div[1]/div[2]/div[2]/ul/li')
        for li in div_list:
            name = li.xpath('.//a/text()').extract_first()
            print(name)
            detail_url='http://www.nanhujng.com/clzl/jbcl/202101/t20210115_719646.shtml'
            #detail_url='http://www.qzhjg.cn'+detail_url
            #print(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,dont_filter=True,meta={'item':item})
    def parse_detail(self, response):
        img=response.xpath('//img/@src').extract()
        a=img[self.i]
        a=a[1:len(a)]
        img='https://www.nanhujng.com/clzl/jbcl/202101'+a
        print(img)
        self.i+=1
        cont=''

