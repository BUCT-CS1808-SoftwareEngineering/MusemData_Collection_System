import scrapy
from museum.items import collectionItem
#解析数据为空
class Collection112Spider(scrapy.Spider):
    name = 'collection112'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://museum.linyi.cn/dzjp/tq.htm']

    url = 'http://museum.linyi.cn/dzjp/tq/%d.htm'
    page_num = 1
    def parse_detail(self, response):
        item = response.meta["item"]    
        if response.xpath('/html/body/div[3]/div/div[2]/form/table/tbody/tr[4]/td/div/div/div/p//text()'):
            coll_desc = response.xpath('/html/body/div[3]/div/div[2]/form/table/tbody/tr[4]/td/div/div/div/p//text()').extract()
            coll_desc = ''.join(coll_desc)
            print(coll_desc)  

    def parse(self, response):
        item = collectionItem()          
        coll_list = response.xpath('/html/body/div[3]/div/div[2]/table[1]/tbody/tr/td/div/table/tbody/tr[1]/td')
        coll_name = response.xpath('/html/body/div[3]/div/div[2]/table[1]/tbody/tr/td/div/table/tbody/tr[1]/td[1]/span/a/span/text()').extract_first()
        print(coll_name)
        #/html/body/div[3]/div/div[2]/table[1]/tbody/tr/td/div/table/tbody/tr[1]/td[1]
        for div in coll_list:
           
            coll_name = div.xpath('./span/a/span/text()').extract_first()
            print(coll_name)

            coll_img =  div.xpath('./table/tbody/tr/td/a/img/@src').extract_first()          
            print(coll_img)
           
            detail_url =  div.xpath('./table/tbody/tr/td/a/@href').extract_first()
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})

        if self.page_num <= 4:
            new_url = (self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)
