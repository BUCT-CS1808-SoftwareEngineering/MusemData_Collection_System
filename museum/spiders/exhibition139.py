import scrapy
from museum.items import exhibitionItem
#scrapy crawl collection
#scrapy crawl exhiition
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
#scrapy genspider education
class Education9Spider(scrapy.Spider):
    name = 'exhibition139'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.westlakemuseum.com/index.php/bwggk/bwgjj']

    def parse(self, response):
        item = exhibitionItem()
        #scrapy crawl exhibition139
        div_list = response.xpath('/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div[2]/table')
        i=0
        for li in div_list:
            i+=1
            if i==4 or i==5 or i==7 or i==8 or i==9:
                name = li.xpath('.//text()').extract()
                name=''.join(name)
                name=name[0:30]
                print(name)
                img = li.xpath('.//img/@src').extract_first()
                if img:
                    img='http://www.westlakemuseum.com'+img
                print(img)
                cont=li.xpath('.//text()').extract()
                cont=''.join(cont)
                cont=cont.replace(name,'')
                cont=str.strip(cont)
                print(cont)

