import scrapy
from  selenium import webdriver 
from museum.items import exhibitionItem 
# import re
# scrapy crawl exhibition14

class Exhibition14Spider(scrapy.Spider):
    name = 'exhibition14'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://39.98.66.177/QinLing/PhotoGallery']

    # start_urls = ['http://39.98.66.177/QinLing/PhotoGallery']
    new_urls = []
    deep_urls = []
    js1_urls = []
    js2_urls = []
    js3_urls = ['http://39.98.66.177/QinLing/PhotoGallery']
    # deep_urls = []

    # def start_requests(self):
    #     url = 'http://www.njmuseum.com/zh/educationIndex'
    #     # FormRequest 是Scrapy发送POST请求的方法，但是没有解决问题
    #     # yield scrapy.FormRequest(
    #     #     headers={'Content-Type': 'application/json'},
    #     #     method = 'POST',
    #     #     url = IP_PORT,
    #     #     formdata = json.dumps(self.data)
    #     #     callback = self.parse
    #     #     # dont_filter = True
    #     # )
 
    #     # 最后不得不采用request直接解决了。。
        # yield scrapy.Request(url = IP_PORT, method='POST',callback = self.parse)

    #实例化一个
    def __init__(self):
        self.bro = webdriver.Firefox()
    def parse(self, response):
        item = exhibitionItem()
        # /html/body/section[2]/div[2]/div[2]/ul
        li_list = response.xpath('/html/body/div/div[2]/div/div[3]/div/div[2]/div[1]/div/ul/li')
        # print(li_list)
        # xp = '/html/body/div[1]/div/div[3]/div/div'
        # num = 1
        for li in li_list:
            name = li.xpath('./a/h3/text()').extract()
            name = ''.join(name)
            print(name)
            img = li.xpath('./a/img/@src').extract()
            img = ''.join(img)
            img = 'http://39.98.66.177' + img
            print(img)
            cont = 'None'
            # cont = ''.join(cont)
            print(cont)
            # item['exhibName'] = name
           
            # item['exhibImg'] = img

    def closed(self,spider):
        self.bro.quit()
        # self.brom.quit()

