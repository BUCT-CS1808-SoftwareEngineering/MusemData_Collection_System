import scrapy
from museum.items import collectionItem
import re
# scrapy crawl collection23

class Collection23Spider(scrapy.Spider):
    name = 'collection23'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.nanhaimuseum.org/411890/417410/index1.html']

    url = 'http://www.nanhaimuseum.org/411890/417410/index%d.html'
    page_num = 2

    def parse_detail(self, response):
        item = response.meta["item"]
        coll_name = response.xpath('/html/body/div/div[2]/div[1]/div[2]/h1/text()').extract_first()
        coll_name = re.sub('&(.+?);','',coll_name)
        print(coll_name)
        coll_img = response.xpath('/html/body/div/div[2]/div[1]/div[2]/div[4]/p[1]/span/img/@src').extract_first()
        coll_img = 'http://www.nanhaimuseum.org' + coll_img
        print(coll_img)
        # if response.xpath('//*[@id="intro"]//text()'):
        coll_desc = response.xpath('/html/body/div/div[2]/div[1]/div[2]/div[4]//text()').extract()
        coll_desc = ''.join(coll_desc)
        print(coll_desc)
            
        # yield item

    def parse(self, response):
        item = collectionItem()
        coll_list = response.xpath('//*[@id="tiles"]/li')
        for li in coll_list:
            detail_url = li.xpath('./a/@href').extract_first()
            # print(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        
        if self.page_num <= 2:
            new_url = (self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)
