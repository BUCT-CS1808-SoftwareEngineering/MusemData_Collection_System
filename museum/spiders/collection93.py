import scrapy
from museum.items import collectionItem

#只能爬取一个藏品，当爬取多个时候输出为none
class Collection93Spider(scrapy.Spider):
    name = 'collection93'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.aybwg.org/photo/list.php?catid=40']
    #url = 'http://www.aybwg.org/photo/list.php?catid=40&page=%d'
    #page_num = 2

    def parse(self, response):
        item = collectionItem()
                                   #/html/body/div/div[4]/div[2]/div/ul/li[3]/a/span
                                   #/html/body/div/div[4]/div[2]/div/ul/li[2]/a/span
        #coll_list = response.xpath('/html/body/div[3]/div[4]/ul/li')
        coll_name = response.xpath('/html/body/div/div[4]/div[2]/div/ul/li[1]/a/span/text()').extract_first()
        print(coll_name)
        coll_img = response.xpath('/html/body/div/div[4]/div[2]/div/ul/li[1]/a/div/img/@src').extract_first()
        print(coll_img)
        #for li in coll_list:
            #./div/p/a
            #coll_name = li.xpath('./a/span/text()').extract_first()
            #print(coll_name)
            #./div/span/a/img
            #coll_img = li.xpath('./a/div/img/@src').extract_first()
            #coll_img = 'http://www.pdsm.org.cn' + coll_img
            #print(coll_img)
            #/div/span/a
            #藏品无描述
            #detail_url = 'http://61.187.53.122/' + li.xpath('./div/span/a/@href').extract_first()
            #yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        
        #if self.page_num <= 10:
            #new_url = (self.url%self.page_num)
            #self.page_num += 1
            #yield scrapy.Request(new_url,callback=self.parse)

        
