import scrapy
from museum.items import exhibitionItem 
#scrapy crawl collection
#scrapy crawl exhiition
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
#scrapy genspider education
class Education9Spider(scrapy.Spider):
    name = 'exhibition133'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.ahbbmuseum.com/?list_16/']

    def parse(self, response):
        item = exhibitionItem()
        #scrapy crawl exhibition133
        div_list = response.xpath('/html/body/div[2]/div[2]/div/div/div[2]/ul/li')
        cnt=0
        for li in div_list:
             cnt+=1;
             if(cnt==7):break
             name = li.xpath('.//a/text()').extract_first()
             print(name)
             detail_url=li.xpath('.//a/@href').extract_first()
             detail_url='https://www.ahbbmuseum.com'+detail_url
             #print(detail_url)
             yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
    def parse_detail(self, response):
        item = response.meta["item"]
        img = response.xpath('//*[@class="content"]//img/@src').extract_first()
        img='https://www.ahbbmuseum.com'+img
        print(img)
        cont=response.xpath('//*[@class="content"]//p//text()').extract()
        cont = ''.join(cont)
        print(cont)