import scrapy
from museum.items import educationItem
#scrapy crawl collection
#scrapy crawl exhiition
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
#scrapy genspider education
class Education9Spider(scrapy.Spider):
    name = 'exhibition148'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.chinasilkmuseum.com/zz/list_17.aspx']

    def parse(self, response):
        item = educationItem()
        #scrapy crawl exhibition148
        div_list = response.xpath('/html/body/div[1]/div/div[2]/div/ul/li')
        for li in div_list:
            name = li.xpath('./div/h3/a/text()').extract_first()
            print(name)
            img=li.xpath('.//img/@src').extract_first()
            img='https://www.chinasilkmuseum.com'+img
            print(img)
            detail_url=li.xpath('.//a/@href').extract_first()
            detail_url='https://www.chinasilkmuseum.com'+detail_url
            print(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
    def parse_detail(self, response):
        item = response.meta["item"]
        #img = response.xpath('//*[@class="nr"]//img/@src').extract_first()
        #print(img)
        cont=response.xpath('//*[@class="detail_text"]//text()').extract()
        cont = ''.join(cont)
        print(cont)