import scrapy
from museum.items import exhibitionItem 
#scrapy crawl collection
#scrapy crawl exhiition
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
#scrapy genspider education
class Education9Spider(scrapy.Spider):
    name = 'exhibition129'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.gthyjng.com/shjy/xxjyhd/']

    def parse(self, response):
        item = exhibitionItem()
        #scrapy crawl exhibition129
        div_list = response.xpath('/html/body/div[4]/div/div[2]/div[2]/ul/li')
        for li in div_list:
            name = li.xpath('./h1/text()').extract_first()
            name=name[5:len(name)]
            name=str.strip(name)
            print(name)
            detail_url=li.xpath('./p//@href').extract_first()
            print(detail_url)
            img='https://mmbiz.qpic.cn/mmbiz_jpg/rnN3IJL45SNWKW5CibNDqOZhpmojjEhV1iaqeVDUGUDufkaqFqOv7XuwR2HTtMjGEYFDz4dnNsq7OicCoMLjpCnNg/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1'
            cont=detail_url
            print(img)