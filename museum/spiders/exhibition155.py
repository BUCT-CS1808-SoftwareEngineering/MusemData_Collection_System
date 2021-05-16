import scrapy
from museum.items import educationItem
#scrapy crawl collection
#scrapy crawl exhiition
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
#scrapy genspider education
class Education9Spider(scrapy.Spider):
    name = 'exhibition155'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.xzmuseum.com/zl.aspx?category_id=495']

    def parse(self, response):
        item = educationItem()
        #scrapy crawl exhibition155
        div_list = response.xpath('/html/body/div[4]/div/div[2]/div[2]/div[2]/div')
        for li in div_list:
            name = li.xpath('.//h2/a/text()').extract_first()
            print(name)
            img=li.xpath('.//img/@src').extract_first()
            img='https://www.xzmuseum.com'+img
            print(img)
            detail_url=li.xpath('.//a/@href').extract_first()
            detail_url='https://www.xzmuseum.com'+detail_url
            print(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
    def parse_detail(self, response):
        item = response.meta["item"]
        #img = response.xpath('//*[@class="nr"]//img/@src').extract_first()
        #print(img)
        cont=response.xpath('//*[@class="del_f"]//text()').extract()
        cont = ''.join(cont)
        print(cont)