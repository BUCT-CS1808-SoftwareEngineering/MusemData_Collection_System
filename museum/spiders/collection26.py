import scrapy
from museum.items import collectionItem
import re
# scrapy crawl collection26

class Collection26Spider(scrapy.Spider):
    name = 'collection26'
    start_urls = ['http://www.njiemuseum.com/index.php/Index/Index/col/c_id/45/page/1.html']
    url = 'http://www.njiemuseum.com/index.php/Index/Index/col/c_id/45/page/%d.html'
    page_num = 2

    def parse_detail(self, response):
        item = response.meta["item"]
        # if response.xpath('//*[@id="intro"]//text()'):
        coll_desc = 'None'
        if response.xpath('//*[@id="ContentPlaceHolder1_cnt"]/div/div[3]//text()').extract():
            coll_desc = response.xpath('//*[@id="ContentPlaceHolder1_cnt"]/div/div[3]//text()').extract()
            coll_desc = ''.join(coll_desc)
        print(coll_desc)
            

    def parse(self, response):
        item = collectionItem()
        coll_list = response.xpath('//*[@id="ContentPlaceHolder1_main_cnt"]/ul/li')
        for li in coll_list:
            name = li.xpath('./div[2]/a/text()').extract_first()
            print(name)
            img = "http://www.njiemuseum.com" + li.xpath('./div[1]/a[1]/img/@src').extract_first()
            print(img)
            detail_url = "http://www.njiemuseum.com" + li.xpath('./div[1]/a[1]/@href').extract_first()
            print(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        
        if self.page_num <= 5:
            new_url = (self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)
