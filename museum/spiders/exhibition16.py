import scrapy
from museum.items import exhibitionItem 
import re
# scrapy crawl exhibition16

class Exhibition16Spider(scrapy.Spider):
    name = 'exhibition16'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.tjbwg.com/cn/ExhibitionList.aspx?TypeId=10939']

    def parse_detail(self, response):
        item = response.meta["item"]
        cont = response.xpath('/html/body/div/div[3]/div/div/div[2]/div[2]/div/div[2]/div[2]//text()').extract()
        cont = ''.join(cont)
        des = response.xpath('/html/body/div/div[3]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[2]//text()').extract()
        des = ''.join(des)
        cont = cont + des
        cont = re.sub('&(.+?);','',cont)
        print(cont)
       
        # yield item


    def parse(self, response):
        item = exhibitionItem()
        div_list = response.xpath('/html/body/div/div[3]/div/div/div[2]/div[2]/div/div/ul/li')
        for div in div_list:
            img = div.xpath('./div/a/div[1]/img/@src').extract_first()
            img = "https://www.tjbwg.com" + img
            print(img)
            name = div.xpath('./div/a/div[2]/h3/text()').extract_first()
            print(name)
            detail_url = div.xpath('./div/a/@href').extract_first()
            detail_url = "https://www.tjbwg.com/cn/" + detail_url
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
