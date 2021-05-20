import scrapy
from museum.items import exhibitionItem
#scrapy crawl collection
#scrapy crawl exhiition
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
#scrapy genspider education
class Education9Spider(scrapy.Spider):
    name = 'exhibition145'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.wzmuseum.cn/Col/Col25/Index.aspx']

    def parse(self, response):
        item = exhibitionItem()
        #scrapy crawl exhibition145
        div_list = response.xpath('/html/body/div[1]/div[4]/div[2]/ul/li')
        for li in div_list:
            name = li.xpath('.//span/text()').extract()
            name=''.join(name)
            print(name)
            img=li.xpath('.//img/@src').extract_first()
            img='http://www.wzmuseum.cn'+img
            print(img)
            cont=li.xpath('.//text()').extract()
            cont=''.join(cont)
            print(cont)