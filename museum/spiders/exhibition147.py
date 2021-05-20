import scrapy
from museum.items import exhibitionItem
#scrapy crawl collection
#scrapy crawl exhibition147
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
#scrapy genspider education
class Education9Spider(scrapy.Spider):
    name = 'exhibition147'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.nbmuseum.cn/jbcl/allnb.html','http://www.nbmuseum.cn/jbcl/zkys.html','http://www.nbmuseum.cn/jbcl/dfsz.html']

    def parse(self, response):
        item = exhibitionItem()
        #/html/body/div[3]/div/div[2]/table[1]/tbody/tr[1]/td
        name=response.xpath('/html/body/div[3]/div/div[2]/table[1]//text()').extract()
        name=name[2]
        print(name)
        img=response.xpath('//img/@src').extract()
        img=img[1]
        if img[0]!='h':
            img='http://www.nbmuseum.cn'+img
        print(img)
        cont=response.xpath('/html/body/div[3]/div/div[2]/table[2]//text()').extract()
        cont=''.join(cont)
        print(cont)