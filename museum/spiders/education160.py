import scrapy
from museum.items import educationItem
#scrapy crawl collection
#scrapy crawl exhiition
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
#scrapy genspider education
class Education9Spider(scrapy.Spider):
    name = 'education160'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.shmmc.com.cn/Home/NewsList_Jy?condition=3']

    def parse(self, response):
        item = educationItem()
        #scrapy crawl education160
        div_list = response.xpath('/html/body/div[2]/div[2]/div/div[2]/div[2]/div[1]/ul/li')
        for li in div_list:
            name = li.xpath('./a/text()').extract_first()
            print(name)
            detail_url=li.xpath('./a/@href').extract_first()
            detail_url='https://www.shmmc.com.cn'+detail_url
            print(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
    def parse_detail(self, response):
        item = response.meta["item"]
        img = response.xpath('//*[@id="view_news"]//img/@src').extract_first()
        #if(img):
            #img='https://www.shmmc.com.cn'+img
        print(img)
        cont=response.xpath('//*[@id="view_news"]//text()').extract()
        cont = ''.join(cont)
        print(cont)
