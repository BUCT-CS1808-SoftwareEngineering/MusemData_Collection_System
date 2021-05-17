import scrapy
import re
from museum.items import MuseumItem
import pandas as pd
from selenium import webdriver
import os
import urllib

path = os.path.realpath(os.curdir)#获取当前目录的绝对路径

path = os.path.join(path, "muselist.xlsx")#加上文件名
#scrapy crawl baikePic

def get_list():

    df = pd.read_excel(path, usecols=[1], engine='openpyxl')
    data = df.values
    muse_list = []
    # print(type(data))
    # print(data)
    for i in data:
        i = list(i)
        # print(type(i))
        # print(i)
        if type(i[0]) is not type('博物馆'):
            continue
        muse_list.append(i[0])

    return muse_list

class BaikepicSpider(scrapy.Spider):
    name = 'baikePic'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://pic.sogou.com/pics?query=%E6%95%85%E5%AE%AB']
    new_urls = ['https://pic.sogou.com/pics?query=%E6%95%85%E5%AE%AB']
    url = 'https://pic.sogou.com/pics?query='
    mus_name = get_list()

    num = 0

    def __init__(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        self.bro = webdriver.Firefox(options=options)
        # self.brom = webdriver.Firefox(options=options)

    def parse(self, response):
        item = MuseumItem()
        item['img'] = '暂无'
        if self.num == 0:
            item['museumID'] = 1
        else:
            item['museumID'] = response.meta['num']
            # name1 = str(response.meta['name'])
            # if name1 == '南通博物馆':
            #     name1 = '南通博物苑'
        self.num += 1
        # item['museumName'] = name1
        item['img'] = response.xpath('//*[@id="videoApp"]/div/div[2]/div/ul/li[2]/div/a[1]/img/@src').extract_first()
        print(item['img'])
        yield item


        # mus_name = ['中国国家博物馆','上海科技馆','中央苏区（闽西）历史博物馆']
        # print(mus_name)
        for i in range(len(self.mus_name)):
        # for i in range(2):
            if i == 0:
                continue
            name = urllib.parse.quote(str(self.mus_name[i]))
            url_use = self.url + name
            self.new_urls.append(url_use)
            yield scrapy.Request(url_use,callback=self.parse,meta = {'name':name,'num':i+1})
    
    def closed(self,spider):
        self.bro.quit()
