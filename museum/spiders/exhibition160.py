import scrapy
from museum.items import exhibitionItem
#scrapy crawl collection
#scrapy crawl exhiition
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
#scrapy genspider education
class Education9Spider(scrapy.Spider):
    name = 'exhibition160'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.shmmc.com.cn/Home/CszgList']

    def parse(self, response):
        item = exhibitionItem()
        #scrapy crawl exhibition160
        div_list = response.xpath('/html/body/div[2]/div[2]/div/div[2]/div[2]/div/div')
        for li in div_list:
            name = li.xpath('.//b/text()').extract_first()
            if not name:
                break
            print(name)
            img=li.xpath('.//img/@src').extract_first()
            img='https://www.shmmc.com.cn'+img
            print(img)
            cont=response.xpath('//span//text()').extract()
            cont = ''.join(cont)
            print(cont)