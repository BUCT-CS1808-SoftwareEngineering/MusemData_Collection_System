import scrapy
from museum.items import collectionItem
# scrapy crawl collection7

class Collection7Spider(scrapy.Spider):
    name = 'collection7'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.sxhm.com/index.php?page=1&ac=article&at=list&tid=218']
    url = 'http://www.sxhm.com/index.php?page=%d&ac=article&at=list&tid=218'
    page_num = 2

    def parse_detail(self, response):
        item = response.meta["item"]
        # coll_name = response.xpath('//*[@id="hl_content"]/div/div[2]/h3/span/text()').extract_first()
        coll_desc = response.xpath('/html/body/div[3]/div[2]/div[2]/div[3]//text()').extract()
        coll_desc = ''.join(coll_desc)
        # coll_img = response.xpath('/html/body/div[3]/div[2]/div[2]/div[3]/p[2]/img/@src').extract_first()
        # coll_img = 'http://www.sxhm.com' + coll_img
        # print(coll_name)
        print(coll_desc)
        # print(coll_img)
        # yield item

    def parse(self, response):
        item = collectionItem()
        # //*[@id="building2"]/div/div[2]/table/tbody
        coll_list = response.xpath('/html/body/div[3]/div[2]/div[2]/ul/li')
        for li in coll_list:
            if li.xpath('./a/span/text()').extract_first() != None:
                # //*[@id="227613"]/text()
                coll_name = li.xpath('./a/span/text()').extract_first()
                # coll_name = ''.join(coll_name)
                print(coll_name)
                coll_img = li.xpath('./a/img/@src').extract_first()
                coll_img = 'http://www.sxhm.com' + coll_img
                print(coll_img)
            # print(li.xpath('./td/a/@href').extract_first())
                detail_url = li.xpath('./a/@href').extract_first()
                yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        
        if self.page_num <= 2:
            new_url = (self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)

