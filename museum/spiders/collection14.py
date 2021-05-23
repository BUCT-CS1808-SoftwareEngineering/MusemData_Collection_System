import scrapy
from museum.items import collectionItem
from selenium import webdriver
#scrapy crawl collection14

class Collection14Spider(scrapy.Spider):
    name = 'collection14'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.bmy.com.cn/html/gov/zwgk/zpxxgk/44f6ddedd33c418f91653bee29ec283f.html']

    new_urls = ['http://www.bmy.com.cn/html/gov/zwgk/zpxxgk/44f6ddedd33c418f91653bee29ec283f.html']
    deep_urls = []
    # url = 'http://www.zhejiangmuseum.com/Collection/ExcellentCollection?page=%d'
    # page_num = 2

    #实例化一个
    def __init__(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        self.bro = webdriver.Firefox(options=options)
        # self.brom = webdriver.Firefox()

    def parse(self, response):
        # //*[@id="building2"]/div/div[2]/table/tbody
        coll_list = response.xpath('/html/body/div[2]/div[2]/div[3]/div')
        # print(coll_list)
        for li in coll_list:
            item = collectionItem()
            # if li.xpath('./td/a/text()').extract_first() != None:
                # //*[@id="227613"]/text()
            coll_name = li.xpath('./div[2]/p/span[2]/text()').extract_first()
            # coll_name = ''.join(coll_name)
            print(coll_name)
            # print(li.xpath('./td/a/@href').extract_first())
            # detail_url = 'http://www.zhejiangmuseum.com' + li.xpath('./a/@href').extract_first()
            img = li.xpath('./div[1]/img/@src').extract_first()
            # if img[0] == '/':
            # img = 'http://www.zhejiangmuseum.com' + img
            print(img)
            cont = "时代：" + li.xpath('./div[2]/p[3]/span[2]/text()').extract_first() + "\n级别：" + li.xpath('./div[2]/p[4]/span[2]/text()').extract_first() + "\n现状：" + li.xpath('./div[2]/p[5]/span[2]/text()').extract_first()
            print(cont)
            item['collectionName']=coll_name
            item['museumID']=14
            item['collectionImage']=img
            item['collectionIntroduction']=cont
            yield item
            # self.deep_urls.append(detail_url)
            # yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        
        # if self.page_num <= 291:
        #     new_url = (self.url%self.page_num)
        #     self.page_num += 1
        #     self.new_urls.append(new_url)
        #     yield scrapy.Request(new_url,callback=self.parse)

    # def parse_detail(self, response):
    #     item = response.meta["item"]
    #     # coll_name = response.xpath('//*[@id="hl_content"]/div/div[2]/h3/span/text()').extract_first()
    #     time = 'None'
    #     if response.xpath('//*[@id="app"]/div/div/div/div/main/div/div[2]/div[2]/div[1]/div[1]/p/text()').extract():
    #         time = response.xpath('//*[@id="app"]/div/div/div/div/main/div/div[2]/div[2]/div[1]/div[1]/p/text()').extract_first()
    #     coll_desc = response.xpath('//*[@id="app"]/div/div/div/div/main/div/div[3]/text()').extract()
    #     print(coll_desc)
    #     if response.xpath('//*[@id="app"]/div/div/div/div/main/div/div[3]/text()').extract():
    #         coll_desc = ''.join(coll_desc) + ' 年代：' + time 
    #     else:
    #         coll_desc = ' 年代：' + time
    #     # coll_img = response.xpath('//*[@id="hl_content"]/div/div[1]/div/div/div/img/@src').extract_first()
    #     # print(coll_name)
    #     print(coll_desc)
    #     # print(coll_img)
    #     # yield item

    def closed(self,spider):
        self.bro.quit()
        # self.brom.quit()
