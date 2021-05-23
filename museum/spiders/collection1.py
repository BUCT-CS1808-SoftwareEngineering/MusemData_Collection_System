import scrapy
from museum.items import collectionItem

# scrapy genspider collection www.xxx.com
# scrapy genspider exhibition www.xxx.com
# scrapy genspider education www.xxx.com

# scrapy crawl collection1
# 故宫 

class Collection1Spider(scrapy.Spider):
    name = 'collection1'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.dpm.org.cn/collection/ceramics.html']
    # start_urls = ['https://www.dpm.org.cn/collection//category_id/90/p/2.html']
    url = 'https://www.dpm.org.cn/searchs/ceramics/category_id/90/sort/class_sort/dbg/0/p/%d.html'
    new_urls = []
    deep_urls = []
    js1_urls = []
    js2_urls = []
    js3_urls = []
    page_num = 2

    def parse_detail(self, response):
        item = response.meta["item"]
        # coll_name = response.xpath('//*[@id="hl_content"]/div/div[2]/h3/span/text()').extract_first()
        coll_desc = response.xpath('//*[@id="hl_content"]/div/div[2]/div[1]/div[1]/p/text()').extract()
        coll_desc = ''.join(coll_desc)
        coll_img = response.xpath('//*[@id="hl_content"]/div/div[1]/div/div/div/img/@src').extract_first()
        # print(coll_name)
        # print(coll_desc)
        item['collectionIntroduction'] = coll_desc
        if coll_img[0] == '/':
             coll_img = "https://img.dpm.org.cn" + coll_img
        print(item['collectionIntroduction'])
        # print(coll_img)
        item['collectionImage'] = coll_img
        print(item['collectionImage'])
        yield item

    def parse(self, response):
        
        # //*[@id="building2"]/div/div[2]/table/tbody
        coll_list = response.xpath('//*[@id="building2"]/div/div[2]/table/tbody/tr')
        for li in coll_list:
            if li.xpath('./td/a/text()').extract_first() != None:
                item = collectionItem()
                # //*[@id="227613"]/text()
                coll_name = li.xpath('./td/a/text()').extract_first()
                # coll_name = ''.join(coll_name)
                # print(coll_name)
                item['collectionName'] = coll_name
                print(item['collectionName'])
                item['museumID'] = 1
            # print(li.xpath('./td/a/@href').extract_first())
                detail_url = 'https://www.dpm.org.cn/' + li.xpath('./td/a/@href').extract_first()
                yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        
        if self.page_num <= 50:
            new_url = (self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)