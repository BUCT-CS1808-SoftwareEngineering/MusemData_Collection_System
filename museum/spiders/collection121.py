import scrapy
from museum.items import collectionItem

class CollectionSpider(scrapy.Spider):
    name = 'collection121'
    start_urls = ['http://www.zgtcbwg.com/index.php?s=/Home/Article/lists/category/ancientceramics/p/1.html']
    url='http://www.zgtcbwg.com/index.php?s=/Home/Article/lists/category/ancientceramics/p/%d.html'
    page_num = 2
    
    def parse_detail(self, response):
        #/html/body/div[1]/div/div[2]/div[2]/p[4]
        #/html/body/div[1]/div/div[2]/div[2]/p[2]
        x=response.xpath('/html/body/div[1]/div/div[2]/div[2]/p[4]//span/text()').extract()
        #x = "".join(x.split())
        coll_desc=''
        n=len(x)
        for i in x:
            if i!=None:
                coll_desc+=i
        x=response.xpath('/html/body/div[1]/div/div[2]/div[2]//img/@src').extract_first()
        coll_img='http://www.zgtcbwg.com/'+x
        #print(coll_name)
        print(coll_desc)
        print(coll_img)
    def parse(self, response):
        item = collectionItem()
        coll_list = response.xpath('//*[@class="row mt20"]/div')
        for li in coll_list:
            if li.xpath('./a/p[1]/text()').extract_first()!=None:
                coll_name=li.xpath('./a/p[1]/text()').extract_first()
                print(coll_name)
                detail_url = 'http://www.zgtcbwg.com/' + li.xpath('./a/@href').extract_first()
                yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
                
        if self.page_num <= 3:
            new_url = (self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)
