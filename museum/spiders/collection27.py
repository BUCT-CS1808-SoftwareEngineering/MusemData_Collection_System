import scrapy
from museum.items import collectionItem
import re
# scrapy crawl collection27

class Collection27Spider(scrapy.Spider):
    name = 'collection27'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.portmuseum.cn/cp_list.php?catg=1&types=1',
    'http://www.portmuseum.cn/cp_list.php?catg=1&types=2',
    'http://www.portmuseum.cn/cp_list.php?catg=1&types=3',
    'http://www.portmuseum.cn/cp_list.php?catg=1&types=4',
    'http://www.portmuseum.cn/cp_list.php?catg=1&types=5']

    def parse_detail(self, response):
        item = response.meta["item"]
        # if response.xpath('//*[@id="intro"]//text()'):
        coll_desc = 'None'
        if response.xpath('/html/body/div[3]/div[3]//text()').extract():
            coll_desc = response.xpath('/html/body/div[3]/div[3]//text()').extract()
            coll_desc = ''.join(coll_desc)
        print(coll_desc)
            

    def parse(self, response):
        item = collectionItem()
        coll_list = response.xpath('/html/body/div[3]/div[2]/ul/li')
        for li in coll_list:
            name = li.xpath('./a/div/h3/text()').extract_first()
            print(name)
            img = "http://www.portmuseum.cn" + li.xpath('./a/img/@src').extract_first()
            print(img)
            detail_url = "http://www.portmuseum.cn/" + li.xpath('./a/@href').extract_first()
            print(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
    
