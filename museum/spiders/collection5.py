import scrapy
from museum.items import collectionItem
from selenium import webdriver
#scrapy crawl collection5
class Collection5Spider(scrapy.Spider):
    name = 'collection5'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.zhejiangmuseum.com/Collection/ExcellentCollection?page=1']
    new_urls = ['http://www.zhejiangmuseum.com/Collection/ExcellentCollection?page=1']
    deep_urls = []
    url = 'http://www.zhejiangmuseum.com/Collection/ExcellentCollection?page=%d'
    page_num = 2

    #实例化一个
    def __init__(self):
        self.bro = webdriver.Firefox()
        self.brom = webdriver.Firefox()

    def parse(self, response):
        item = collectionItem()
        # //*[@id="building2"]/div/div[2]/table/tbody
        coll_list = response.xpath('//*[@id="app"]/div/div/div/div/main/ul/li[@class="col-list-i"]')
        # print(coll_list)
        for li in coll_list:
            # if li.xpath('./td/a/text()').extract_first() != None:
                # //*[@id="227613"]/text()
            coll_name = li.xpath('./a/h3/text()').extract_first()
            # coll_name = ''.join(coll_name)
            print(coll_name)
            # print(li.xpath('./td/a/@href').extract_first())
            detail_url = 'http://www.zhejiangmuseum.com' + li.xpath('./a/@href').extract_first()
            img = li.xpath('./a/figure/img/@src').extract_first()
            if img[0] == '/':
                img = 'http://www.zhejiangmuseum.com' + img
            print(img)
            self.deep_urls.append(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        
        if self.page_num <= 291:
            new_url = (self.url%self.page_num)
            self.page_num += 1
            self.new_urls.append(new_url)
            yield scrapy.Request(new_url,callback=self.parse)

    def parse_detail(self, response):
        item = response.meta["item"]
        # coll_name = response.xpath('//*[@id="hl_content"]/div/div[2]/h3/span/text()').extract_first()
        time = 'None'
        if response.xpath('//*[@id="app"]/div/div/div/div/main/div/div[2]/div[2]/div[1]/div[1]/p/text()').extract():
            time = response.xpath('//*[@id="app"]/div/div/div/div/main/div/div[2]/div[2]/div[1]/div[1]/p/text()').extract_first()
        coll_desc = response.xpath('//*[@id="app"]/div/div/div/div/main/div/div[3]/text()').extract()
        print(coll_desc)
        if response.xpath('//*[@id="app"]/div/div/div/div/main/div/div[3]/text()').extract():
            coll_desc = ''.join(coll_desc) + ' 年代：' + time 
        else:
            coll_desc = ' 年代：' + time
        # coll_img = response.xpath('//*[@id="hl_content"]/div/div[1]/div/div/div/img/@src').extract_first()
        # print(coll_name)
        print(coll_desc)
        # print(coll_img)
        # yield item

    def closed(self,spider):
        self.bro.quit()
        self.brom.quit()