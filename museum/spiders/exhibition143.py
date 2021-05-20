import scrapy
from museum.items import exhibitionItem
#scrapy crawl collection
#scrapy crawl exhiition
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
#scrapy genspider education
class Education9Spider(scrapy.Spider):
    name = 'exhibition143'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.teamuseum.cn/information/information_list.htm']

    def parse(self, response):
        item = exhibitionItem()
        #scrapy crawl exhibition143
        div_list = response.xpath('/html/body/div[4]/div[2]/ul/li')
        for li in div_list:
            name = li.xpath('.//h2/text()').extract_first()
            print(name)
            img=li.xpath('.//img/@src').extract_first()
            #img='http://www.qzhjg.cn'+img
            print(img)
            detail_url=li.xpath('.//a/@href').extract_first()
            detail_url='http://www.teamuseum.cn'+detail_url
            print(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
    def parse_detail(self, response):
        item = response.meta["item"]
        #img = response.xpath('//*[@class="nr"]//img/@src').extract_first()
        #print(img)
        cont=response.xpath('//*[@class="kp_dl_cnt"]//text()').extract()
        cont = ''.join(cont)
        print(cont)