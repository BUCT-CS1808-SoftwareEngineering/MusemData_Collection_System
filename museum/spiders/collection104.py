import scrapy
from museum.items import collectionItem
#解析数据为none
class Collection104Spider(scrapy.Spider):
    name = 'collection104'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.tengzhoumuseum.com/productlist/list-10-1.html']

    url = 'http://www.tengzhoumuseum.com/productlist/list-10-%d.html'
    page_num = 2
    

    def parse(self, response):
        item = collectionItem()
        coll_list = response.xpath('/html/body/table[4]/tbody/tr/td[3]/table/tbody/tr[1]/td/table[2]/tbody/tr[1]/td/table')
        #name = response.xpath('/html/body/table[4]/tbody/tr/td[3]/table/tbody/tr[1]/td/table[2]/tbody/tr[1]/td/table[1]/tbody/tr[2]/td/a/text').extract_first()
        #print(name)
        for div in coll_list:
            #/tbody/tr[2]/td/a
            coll_name = div.xpath('.//tbody/tr[2]/td/a/text()').extract_first()
            print(coll_name)
            #detail_url = 'http://museum.sdu.edu.cn/' + div.xpath('./div[2]/a/@href').extract_first()
            #/tbody/tr[1]/td/a/img
            coll_img = div.xpath('./tbody/tr[1]/td/a/img/@src').extract_first()
            coll_img = 'http://www.tengzhoumuseum.com' + coll_img
            print(coll_img)
            #yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})

        if self.page_num <= 10:
            new_url = (self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)
