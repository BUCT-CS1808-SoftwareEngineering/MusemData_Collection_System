import scrapy
from museum.items import educationItem
#scrapy crawl collection
#scrapy crawl exhiition
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
#scrapy genspider education
class Education9Spider(scrapy.Spider):
    name = 'education138'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.ahm.cn/Activity/NewsList/sjhd']

    def parse(self, response):
        item = educationItem()
        #scrapy crawl education138
        div_list = response.xpath('/html/body/div[3]/div/div[3]/ul/li')
        for li in div_list:
            name = li.xpath('.//h3/text()').extract_first()
            print(name)
            img=li.xpath('.//img/@src').extract_first()
            #img='http://www.qzhjg.cn'+img
            print(img)
            cont=li.xpath('./div[1]/p/text()').extract_first()
            x=cont.find("活动对象")
            cont=cont[0:x]
            print(cont)