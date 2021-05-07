import scrapy
from museum.items import collectionItem
import re
from selenium import webdriver
# scrapy crawl collection12
class Collection12Spider(scrapy.Spider):
    name = 'collection12'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.ssmzd.com/jngwwjx/jngwwcl/Index.html']

    url = 'http://www.ssmzd.com/jngwwjx/jngwwcl/Index_%d.html'
    # cot = 0
    # page_num = 2
    # co_list = ['qtq','tq','yq','cq','sk','qt']
    # co_page = [10,8,3,4,1,2]

    # def parse_detail(self, response):
    #     item = response.meta["item"]
    #     # coll_name = response.xpath('//*[@id="hl_content"]/div/div[2]/h3/span/text()').extract_first()
    #     # if response.xpath('//*[@id="doZoom"]//text()'):
    #     coll_desc = response.xpath('/html/body/div[7]/div[3]/div[3]/div[2]//text()').extract()
    #     coll_desc = ''.join(coll_desc)
    #     # print(coll_name)
    #     print(coll_desc)
            
        # yield item
    # start_urls = ['http://www.njmuseum.com/zh/collectionList']
    new_urls = ['http://www.ssmzd.com/jngwwjx/jngwwcl/Index.html']
    deep_urls = []
    js1_urls = []
    # url = 'http://www.njmuseum.com/zh/collectionList'
    page_num = 2

    # headers = {
    #     'Accept':'application/json, text/plain, */*',
    #     'Accept-Encoding':'gzip, deflate',
    #     'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    #     'Cache-Control':'max-age=0',
    #     'Connection':'keep-alive',
    #     'Content-Length':'0',   
    #     'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
    #     'Cookie':'Hm_lvt_7c41442deaa2df2e15f8dfa7484a5cf6=1620131367; Hm_lpvt_7c41442deaa2df2e15f8dfa7484a5cf6=1620131440; JSESSIONID=D52071401DB1DFBB16E023B59250EF93',
    #     'Host':'www.njmuseum.com',
    #     'Origin':'http://www.njmuseum.com',
    #     'Referer':'http://www.njmuseum.com/zh/collectionList',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
    #     'X-Requested-With': 'XMLHttpRequest'
    # }

    # def start_requests(self):
    #     yield scrapy.Request(url=self.start_urls[0], callback=self.parse, headers=self.headers)

    #实例化一个
    def __init__(self):
        self.bro = webdriver.Firefox()
        # self.bro.set_window_size(960, 960)
        # self.brom = webdriver.Firefox()
        
    def parse(self, response):
        # i = 0
        # print(self.page_num)
        # for i in range(112):
        #     self.bro.find_element_by_css_selector('.load-more').click()
        # if self.page_num != 1:
        #     self.bro.find_element_by_class_name('btn-next').click()
        # page = str(self.page_num)
        
        # self.bro.find_element_by_xpath(("//*[text()='%d']")%self.page_num).click()
            # i += 1
        item = collectionItem()
        # //*[@id="building2"]/div/div[2]/table/tbody
        coll_list = response.xpath('/html/body/table[2]/tbody/tr/td/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/div')
        
        # print(coll_list)
        # for i in range(2):
        for div in coll_list:
            # if li.xpath('./td/a/text()').extract_first() != None:
                # //*[@id="227613"]/text()
            coll_name = div.xpath('./table/tbody/tr[2]/td/div/a/text()').extract_first()
            # coll_name = ''.join(coll_name)
            print(coll_name)
            # print(li.xpath('./td/a/@href').extract_first())
            # detail_url = 'http://www.njmuseum.com' + div.xpath('./a/@href').extract_first()
            img = div.xpath('./table/tbody/tr[1]/td/table/tbody/tr/td/a/img/@src').extract_first()
            # //*[@id="p_item"]/table/tbody/tr[1]/td/table/tbody/tr/td/a/img
            # if img[0] == '/':
            #     img = 'http://www.zhejiangmuseum.com' + img
            img = 'http://www.ssmzd.com' + img
            print(img)
            cont = 'None'
            # self.deep_urls.append(detail_url)
            # yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
            # self.bro.find_element_by_class_name('btn-next').click()
        # if self.page_num <= 3:
        #     # new_url = (self.url%self.page_num)
        if self.page_num <= 3:
            # new_url = (self.url%(self.co_list[self.cot],self.page_num))
            new_url = (self.url%self.page_num)
            self.new_urls.append(new_url)
            self.page_num += 1
            yield scrapy.Request(new_url,callback=self.parse)
        #     self.page_num += 1
            # self.new_urls.append(new_url)
            # yield scrapy.Request(self.start_urls[0],callback=self.parse)

    # def parse_detail(self, response):
    #     item = response.meta["item"]
    #     # coll_name = response.xpath('//*[@id="hl_content"]/div/div[2]/h3/span/text()').extract_first()
    #     # time = 'None'
    #     # if response.xpath('//*[@id="app"]/div/div/div/div/main/div/div[2]/div[2]/div[1]/div[1]/p/text()').extract():
    #     #     time = response.xpath('//*[@id="app"]/div/div/div/div/main/div/div[2]/div[2]/div[1]/div[1]/p/text()').extract_first()
    #     coll_desc = response.xpath('//*[@id="pdfDom"]/div[2]/div/div//text()').extract()
    #     coll_desc = ''.join(coll_desc)
    #     print(coll_desc)
    #     # if response.xpath('//*[@id="app"]/div/div/div/div/main/div/div[3]/text()').extract():
    #     #     coll_desc = ''.join(coll_desc) + ' 年代：' + time 
    #     # else:
    #     #     coll_desc = ' 年代：' + time
    #     # coll_img = response.xpath('//*[@id="hl_content"]/div/div[1]/div/div/div/img/@src').extract_first()
    #     # print(coll_name)
    #     # print(coll_desc)
    #     # print(coll_img)
        # yield item

    def closed(self,spider):
        self.bro.quit()
        # self.brom.quit()