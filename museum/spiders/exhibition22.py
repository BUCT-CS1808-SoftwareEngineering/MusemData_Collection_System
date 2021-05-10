import scrapy
from museum.items import exhibitionItem
import re 
# scrapy crawl exhibition22

class Exhibition22Spider(scrapy.Spider):
    name = 'exhibition22'
    start_urls = ['https://www.artmuseum.tsinghua.edu.cn/cpsj/zlxx/zzzl/lszl/']

    def parse(self, response):
        item = exhibitionItem()
        li_list = response.xpath('/html/body/div[4]/div[3]/div/ul/li')
        for li in li_list:
            name = li.xpath('./div/h4/a/text()').extract()
            name = ''.join(name)
            print(name)
            img = li.xpath('./a/img/@src').extract_first()
            print(img)
            detail_url = li.xpath('./a/@href').extract_first()
            detail_url = detail_url.replace(".",'',1)
            detail_url = 'https://www.artmuseum.tsinghua.edu.cn/cpsj/zlxx/zzzl/lszl' + detail_url
            # print(detail_url)
            yield scrapy.Request(url=detail_url,callback=self.parse_detail)
    
    def parse_detail(self, response):
        cont = response.xpath('/html/body/div[4]/div[3]/div[1]/div[1]//text()').extract()
        cont = ''.join(cont)
        # cont = re.sub('\n','',cont)
        print(cont)
