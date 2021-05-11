import scrapy
from museum.items import collectionItem
import re
# scrapy crawl collection33

class Collection33Spider(scrapy.Spider):
    name = 'collection33'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.tibetanculturemuseum.org/News_List.php?page=1&tag=Collection&theId=5']
    url = 'http://www.tibetanculturemuseum.org/News_List.php?page=%d&tag=Collection&theId=5'
    page_num = 2

    def parse(self, response):
        item = collectionItem()
        coll_list = response.xpath('//*[@id="collection-lb"]/div[1]/ul/li')
        for li in coll_list:
            if li.xpath('./div[2]/h3/a/text()').extract_first():
                name = li.xpath('./div[2]/h3/a/text()').extract_first()
                print(name)
                img = "http://www.tibetanculturemuseum.org/" + li.xpath('./div[1]/a/img/@src').extract_first()
                print(img)
                cont = li.xpath('./div[2]/span/a//text()').extract()
                cont = ''.join(cont)
                print(cont)
            # detail_url = "http://www.nxbwg.com" + li.xpath('./a/@href').extract_first()
            # print(detail_url)
            # yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        if self.page_num <= 4:
            new_url = (self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)