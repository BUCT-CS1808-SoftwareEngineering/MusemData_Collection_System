# -*- coding: utf-8 -*-
# ajax加载
import scrapy
from selenium import webdriver

class CiaeSpider(scrapy.Spider):
    name = 'collection100'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.ciae.com.cn/collection/detail/zh/1133.html',
                  'https://www.ciae.com.cn/collection/detail/zh/1191.html',
                  'https://www.ciae.com.cn/collection/detail/zh/1562.html',
                  'https://www.ciae.com.cn/collection/detail/zh/2253.html',
                  'https://www.ciae.com.cn/collection/detail/zh/1251.html',
                  'https://www.ciae.com.cn/collection/detail/zh/2413.html',
                  'https://www.ciae.com.cn/collection/detail/zh/2427.html',
                  'https://www.ciae.com.cn/collection/detail/zh/2438.html',
                  'https://www.ciae.com.cn/collection/detail/zh/1741.html',
                  'https://www.ciae.com.cn/collection/detail/zh/2590.html',
                  'https://www.ciae.com.cn/collection/detail/zh/2483.html',
                  'https://www.ciae.com.cn/collection/detail/zh/3012.html',
                  'https://www.ciae.com.cn/collection/detail/zh/1868.html',
                  'https://www.ciae.com.cn/collection/detail/zh/2301.html',
                  'https://www.ciae.com.cn/collection/detail/zh/2330.html',
                  'https://www.ciae.com.cn/collection/detail/zh/2344.html',
                  'https://www.ciae.com.cn/collection/detail/zh/2373.html',
                  'https://www.ciae.com.cn/collection/detail/zh/2567.html']

    model_urls = []
    model_urls = start_urls

    def __init__(self):
        self.bro = webdriver.Chrome(executable_path = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chromedriver.exe')

    def parse(self, response):
        title = response.xpath('/html/body/div[3]/div/div/h3/text()').extract_first()
        img = 'https://www.ciae.com.cn' + response.xpath('/html/body/div[3]/div/div/div[1]/div/img/@src').extract_first()
        content = response.xpath('/html/body/div[3]/div/div/div[2]/h3/text()').extract_first()
        if response.xpath('/html/body/div[3]/div/div/a[2]/@href').extract_first():
            next = 'https://www.ciae.com.cn' + response.xpath('/html/body/div[3]/div/div/a[2]/@href').extract_first()
            print(title, img, next, content)
            yield scrapy.Request(next, callback=self.parse)

    # def parse_detail(self, response):
    #     img = 'https://www.ciae.com.cn' + response.xpath('/html/body/div[3]/div/div/div[1]/div/img/@src').extract_first()
    #     title = response.xpath('/html/body/div[3]/div/div/h3/text()').extract_first()
    #     content = response.xpath('/html/body/div[3]/div/div/div[2]/h3/text()').extract_first()
    #     print(img, title, content)
    #
    # def parse_class(self, response):
    #     li_list = response.xpath('//*[@id="ajax-list"]/ul/li')
    #     print("sajx", li_list)
    #     for i in li_list:
    #         detail_url = 'https://www.ciae.com.cn' + i.xpath('./a/@href').extract_first()
    #         self.model_urls.append(detail_url)
    #         print(detail_url)
    #         yield scrapy.Request(detail_url, callback=self.parse_detail)
    #
    # def parse(self, response):
    #     li_list = response.xpath('//*[@id="ajax-list"]/ul/li')
    #     # print(li_list)
    #     for i in li_list:
    #         class_url = 'https://www.ciae.com.cn' + i.xpath('./a/@href').extract_first()
    #         self.model_urls.append(class_url)
    #         print(class_url)
    #         yield scrapy.Request(class_url, callback=self.parse_class)

    def closed(self,spider):
        self.bro.quit()