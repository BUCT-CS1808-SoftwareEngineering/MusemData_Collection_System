import scrapy
from museum.items import collectionItem
from selenium import webdriver
from lxml import etree
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.support import expected_conditions as expected
# from selenium.webdriver.support.wait import WebDriverWait
# scrapy crawl collection8
class Collection8Spider(scrapy.Spider):
    name = 'collection8'
    # allowed_domains = ['www.xxx.com']
    # start_urls = ['https://www.shanghaimuseum.net/mu/frontend/pg/collection/antique']


    # {"params":{"langCode":"CHINESE","antiqueSourceCode":"ANTIQUE_SOURCE_1"},"page":1,"limit":20}
    start_urls = ['https://www.shanghaimuseum.net/mu/frontend/pg/collection/antique']
    new_urls = []
    deep_urls = []
    js1_urls = []
    js2_urls = ['https://www.shanghaimuseum.net/mu/frontend/pg/collection/antique']
    # url = 'http://www.njmuseum.com/zh/collectionList'
    page_num = 0

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
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        self.bro = webdriver.Firefox(options=options)
        self.brom = webdriver.Firefox(options=options)

        
    def parse(self, response):
        # for i in range(3):
        #     self.bro.find_element_by_css_selector(".layui-flow-more > a:nth-child(1)").click()
        
            # page_text = self.bro.page_source

        # self.bro()
        # print(self.page_num)
        # for i in range(self.page_num):
        #     self.bro.find_element_by_class_name('btn-next').click()
        # if self.page_num != 1:
        #     self.bro.find_element_by_class_name('btn-next').click()
        # page = str(self.page_num)
        
        # self.bro.find_element_by_xpath(("//*[text()='%d']")%self.page_num).click()
            # i += 1
        # //*[@id="building2"]/div/div[2]/table/tbody
        coll_list = response.xpath('//*[@id="list1"]/li')
        # print(coll_list)
        # for i in range(2):
        for div in coll_list:
            item = collectionItem()
            # if li.xpath('./td/a/text()').extract_first() != None:
                # //*[@id="227613"]/text()
            coll_name = div.xpath('./div[1]/div[2]/text()').extract_first()
            # coll_name = ''.join(coll_name)
            print(coll_name)
            item['collectionName'] = coll_name
            item['museumID'] = 8
            # print(li.xpath('./td/a/@href').extract_first())
            detail_url = 'https://www.shanghaimuseum.net/mu/' + div.xpath('./div[1]/div[1]/a/@href').extract_first()
            # img = div.xpath('./div[1]/div[1]/a/img/@src').extract_first()
            # # if img[0] == '/':
            # #     img = 'http://www.zhejiangmuseum.com' + img
            # img = 'https://www.shanghaimuseum.net/mu/' + img
            # print(img)
            self.deep_urls.append(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        # if self.page_num <= 3:
        #     # new_url = (self.url%self.page_num)
            
        #     self.page_num += 1
            # self.new_urls.append(new_url)
            # yield scrapy.Request(self.start_urls[0],callback=self.parse)

    def parse_detail(self, response):
        item = response.meta["item"]
        # coll_name = response.xpath('//*[@id="hl_content"]/div/div[2]/h3/span/text()').extract_first()
        # time = 'None'
        # if response.xpath('//*[@id="app"]/div/div/div/div/main/div/div[2]/div[2]/div[1]/div[1]/p/text()').extract():
        #     time = response.xpath('//*[@id="app"]/div/div/div/div/main/div/div[2]/div[2]/div[1]/div[1]/p/text()').extract_first()
        img = response.xpath('/html/body/div[5]/div/div/div/div[1]/div[1]/div/div/div/a/img/@src').extract_first()
        # img = ''.join(img)
            # if img[0] == '/':
            #     img = 'http://www.zhejiangmuseum.com' + img
        img = 'https://www.shanghaimuseum.net/mu/' + img
        # print(img)
        coll_desc = response.xpath('//*[@id="more"]//text()').extract()
        coll_desc = ''.join(coll_desc)
        # print(coll_desc)
        item['collectionIntroduction'] = coll_desc
        print(item['collectionIntroduction'])
        # print(coll_img)
        item['collectionImage'] = img
        print(item['collectionImage'])
        # if response.xpath('//*[@id="app"]/div/div/div/div/main/div/div[3]/text()').extract():
        #     coll_desc = ''.join(coll_desc) + ' 年代：' + time 
        # else:
        #     coll_desc = ' 年代：' + time
        # coll_img = response.xpath('//*[@id="hl_content"]/div/div[1]/div/div/div/img/@src').extract_first()
        # print(coll_name)
        # print(coll_desc)
        # print(coll_img)
        yield item

    def closed(self,spider):
        self.bro.quit()
        self.brom.quit()
