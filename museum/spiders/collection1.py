import scrapy
from museum.items import collectionItem
# scrapy crawl collection1
# 故宫 

class Collection1Spider(scrapy.Spider):
    name = 'collection1'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.dpm.org.cn/collection/ceramics.html']
    # start_urls = ['https://www.dpm.org.cn/collection//category_id/90/p/2.html']
    url = 'https://www.dpm.org.cn/searchs/ceramics/category_id/90/sort/class_sort/dbg/0/p/%d.html'
    page_num = 2

    def parse_detail(self, response):
        item = response.meta["item"]
        # coll_name = response.xpath('//*[@id="hl_content"]/div/div[2]/h3/span/text()').extract_first()
        coll_desc = response.xpath('//*[@id="hl_content"]/div/div[2]/div[1]/div[1]/p/text()').extract()
        coll_desc = ''.join(coll_desc)
        coll_img = response.xpath('//*[@id="hl_content"]/div/div[1]/div/div/div/img/@src').extract_first()
        # print(coll_name)
        print(coll_desc)
        print(coll_img)
        # yield item

    def parse(self, response):
        item = collectionItem()
        # //*[@id="building2"]/div/div[2]/table/tbody
        coll_list = response.xpath('//*[@id="building2"]/div/div[2]/table/tbody/tr')
        for li in coll_list:
            if li.xpath('./td/a/text()').extract_first() != None:
                # //*[@id="227613"]/text()
                coll_name = li.xpath('./td/a/text()').extract_first()
                # coll_name = ''.join(coll_name)
                print(coll_name)
            # print(li.xpath('./td/a/@href').extract_first())
                detail_url = 'https://www.dpm.org.cn/' + li.xpath('./td/a/@href').extract_first()
                yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        
        if self.page_num <= 110:
            new_url = (self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)