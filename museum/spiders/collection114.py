import scrapy

#需要url的图片和详情页源代码中多了一个"."所以无法进行数据解析
class Collection114Spider(scrapy.Spider):
    name = 'collection114'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.qingzhoumuseum.cn/cp/lxs/index.html']


    #def parse_detail(self, response):
        #item = response.meta["item"]    
        #if response.xpath('/html/body/div[3]/div/div[2]/form/table/tbody/tr[4]/td/div/div/div/p//text()'):
            #coll_desc = response.xpath('/html/body/div[3]/div/div[2]/form/table/tbody/tr[4]/td/div/div/div/p//text()').extract()
            #coll_desc = ''.join(coll_desc)
            #print(coll_desc)  

    def parse(self, response):
        item = collectionItem()          
        coll_list = response.xpath('/html/body/div[3]/table/tbody/tr/td/table/tbody/tr[2]/td')
        #/html/body/div[3]/div/div[2]/table[1]/tbody/tr/td/div/table/tbody/tr[1]/td[1]
        for div in coll_list:
            #table/tbody/tr/td/table/tbody/tr[2]/td/a/span
            coll_name = div.xpath('./table/tbody/tr/td/table/tbody/tr[2]/td/a/span/text()').extract_first()
            print(coll_name)
            #table/tbody/tr/td/div/a/img
            #coll_img = '' + div.xpath('./table/tbody/tr/td/div/a/img/@src').extract_first()          
            #print(coll_img)
           
            #detail_url = '' + div.xpath('./table/tbody/tr/td/div/a/@href').extract_first()
            #yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
