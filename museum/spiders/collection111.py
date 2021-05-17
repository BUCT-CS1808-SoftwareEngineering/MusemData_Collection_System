import scrapy
from museum.items import collectionItem
#详情页无描述
class Collection111Spider(scrapy.Spider):
    name = 'collection111'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.wfsbwg.com/list/?6_1.html']

    url = 'http://www.wfsbwg.com/list/?6_%d.html'
    page_num = 2
    #def parse_detail(self, response):
        #item = response.meta["item"]
                          #/html/body/div[3]/div[3]/div[2]/div[2]/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/p/span[1]         
        #if response.xpath('/html/body/div[3]/div[3]/div[2]/div[2]/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/p/span//text()'):
        #    coll_desc = response.xpath('/html/body/div[3]/div[3]/div[2]/div[2]/div[3]/table/tbody/tr/td/table/tbody/tr/td[2]/p/span//text()').extract()
        #    coll_desc = ''.join(coll_desc)
        #    print(coll_desc)  

    def parse(self, response):
        item = collectionItem()          
        coll_list = response.xpath('/html/body/div[7]/div[2]/div[2]/div[1]/ul/li')
       
        for div in coll_list:
            #/html/body/div[7]/div[2]/div[2]/div[1]/ul/li[5]/a
            coll_name = div.xpath('./a/text()').extract_first()
            print(coll_name)
            #/html/body/div[7]/div[2]/div[2]/div[1]/ul/li[5]/div/a/img
            coll_img = 'http://www.wfsbwg.com'+ div.xpath('./div/a/img/@src').extract_first()
            
            print(coll_img)
            #/html/body/div[2]/div[3]/div[2]/div[2]/ul/li[1]/div[2]/div[1]/a
            #detail_url = 'http://www.wfsbwg.com' + div.xpath('./div/a/@href').extract_first()
            #yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})

        if self.page_num <= 3:
            new_url = (self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)
