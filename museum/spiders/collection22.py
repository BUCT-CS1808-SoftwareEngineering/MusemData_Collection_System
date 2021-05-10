import scrapy
from museum.items import collectionItem
import re
# scrapy crawl collection22

class Collection22Spider(scrapy.Spider):
    name = 'collection22'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.artmuseum.tsinghua.edu.cn/was5/web/search?channelid=261334&page=1&searchword=chnlid=801']
    url = 'http://www.artmuseum.tsinghua.edu.cn/was5/web/search?channelid=261334&page=%d&searchword=chnlid=801'
    cot = 0
    page_num = 2

    def parse(self, response):
        item = collectionItem()
        coll_list = response.xpath('/html/body/ul/li')
        for li in coll_list:
            coll_name = li.xpath('./div[2]/h4/a/text()').extract_first()
            print(coll_name)
            coll_img = li.xpath('./a/img/@src').extract_first()
            coll_img = coll_img
            print(coll_img)
            cont = li.xpath('./div[2]/div//text()').extract()
            cont = ''.join(cont)
            contp = li.xpath('./div[2]/p//text()').extract()
            contp = ''.join(contp)
            cont = cont + contp
            print(cont)
            # yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        
        if self.page_num <= 20:
            # new_url = (self.url%(self.co_list[self.cot],self.page_num))
            new_url = (self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)
