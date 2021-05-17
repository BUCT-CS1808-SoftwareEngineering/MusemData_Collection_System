import scrapy
from museum.items import collectionItem
#详情页描述数据无法解析，但是可以解析详情页名称信息
class Collection102Spider(scrapy.Spider):
    name = 'collection102'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://museum.sdu.edu.cn/gchclist.jsp?totalpage=84&PAGENUM=1&urltype=tree.TreeTempUrl&wbtreeid=1052']
    url = 'http://museum.sdu.edu.cn/gchclist.jsp?totalpage=84&PAGENUM=%d&urltype=tree.TreeTempUrl&wbtreeid=1052'
    page_num = 2
    def parse_detail(self, response):
        item = response.meta["item"]
        
        if response.xpath('/html/body/div[2]/div[2]/form/div[2]/div/p[4]//text()'):
            coll_desc = response.xpath('/html/body/div[2]/div[2]/form/div[2]/div/p[4]//text()').extract()
            coll_desc = ''.join(coll_desc)
            print(coll_desc)  
            #print("1")

    def parse(self, response):
        item = collectionItem()
        coll_list = response.xpath('//*[@id="c"]/div')
        
        for div in coll_list:
            #/html/body/div[3]/div[1]/div[4]/div/form/div[3]/div/div[1]/div[3]/a
            coll_name = div.xpath('./div[3]/a/text()').extract_first()
            print(coll_name)
            detail_url = 'http://museum.sdu.edu.cn/' + div.xpath('./div[2]/a/@href').extract_first()
            coll_img = div.xpath('./div[2]/a/img/@src').extract_first()
            coll_img = 'http://museum.sdu.edu.cn' + coll_img
            print(coll_img)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})

        if self.page_num <= 10:
            new_url = (self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)

        
