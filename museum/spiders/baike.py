import scrapy
import re
from museum.items import MuseumItem
import pandas as pd

import os

path = os.path.realpath(os.curdir)#获取当前目录的绝对路径

path = os.path.join(path, "muselist.xlsx")#加上文件名


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

class BaikeSpider(scrapy.Spider):
    name = 'baike'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://baike.baidu.com/item/%E5%8C%97%E4%BA%AC%E6%95%85%E5%AE%AB%E5%8D%9A%E7%89%A9%E9%99%A2/8663390?fromtitle=%E6%95%85%E5%AE%AB%E5%8D%9A%E7%89%A9%E9%99%A2&fromid=5317'
    ]
    url = 'https://baike.baidu.com/item/'
    # start_urls = ['https://baike.baidu.com/item/%E5%8C%97%E4%BA%AC%E6%95%85%E5%AE%AB%E5%8D%9A%E7%89%A9%E9%99%A2/8663390?fromtitle=%E6%95%85%E5%AE%AB%E5%8D%9A%E7%89%A9%E9%99%A2&fromid=5317'
    # ]
    mus_name = get_list()
    num = 0

    def parse(self, response):
        item = MuseumItem()
        if self.num == 0:
            name1 = self.mus_name[self.num]
        else:
            name1 = str(response.meta['name'])
            if name1 == '南通博物馆':
                name1 = '南通博物苑'
        # name = str(self.mus_name[self.num])
        # /html/body/div[3]/div[2]/div/div[1]/dl[1]/dd/h1
        # name1 = response.xpath('//dd[@class = "lemmaWgt-lemmaTitle-title"]/h1/text()').extract_first()
        # name1 = str(name1)
        self.num += 1
        # name1 = re.findall(u"[\u4e00-\u9fa5]+",name1)
        # m = str(name1)

        # name1 = response.xpath('.').re('<dt class="basicInfo-item name">中文名</dt>\s<dd class="basicInfo-item value">\s(.+?)\s</dd>')
        # name1 = str(name1)
        # name1 = re.findall(u"[\u4e00-\u9fa5]+",name1)
        # m = ''
        # for i in range(len(name1)):
        #     m += str(name1[i])
        # name = name.decode('utf8')
        # print(m)
        item['museumName'] = name1

        # name = response.xpath('.').re('<dt class="basicInfo-item name">外文名</dt>\s<dd class="basicInfo-item value">\s(.+?)\s</dd>')
        # name = str(name)
        # name = re.findall(u"[\u4e00-\u9fa5]+",name)
        # l_name = ''
        # for i in range(len(name)):
        #     m += str(name[i])
        # # name = name.decode('utf8')
        # print(m)

        f_name = response.xpath('.').re('<dt class="basicInfo-item name">外文名</dt>\s<dd class="basicInfo-item value">\s(.+?)\s</dd>')
        if len(f_name):
            f_name = ''.join(f_name)
            f_name = str(f_name)
        else:
            f_name = ''
        # f_name = re.findall(u"[\u4e00-\u9fa5]+",name)
        # lf_name = ''
        # for i in range(len(name)):
        #     m += str(name[i])
        # name = name.decode('utf8')
        # print(f_name)
        item['museumForName'] = f_name


        time = response.xpath('.').re('<dt class="basicInfo-item name">开放时间</dt>\s<dd class="basicInfo-item value">\s([\s\S]*?)\s</dd>')
        time = ''.join(time)
        time = str(time)
        # time = re.sub('<\/?[\s\S]+?\/?>','',time)
        time = re.sub(r'<(\S*)[^>]*>[^<]*<\/(\1)>','',time)
        # print(time)
        item['time'] = time
        location_new = ''
        # |地\xa0\xa0\xa0\xa0点|地\xa0\xa0\xa0\xa0址
        location = response.xpath('.').re('<dt class="basicInfo-item name">(地理位置|地\s*点)</dt>\s<dd class="basicInfo-item value">\s([\s\S]*?)\s</dd>')
        if len(location):
            location_new = str(location[1])
            location_new = re.sub(r'<\/?.+?\/?>','',location_new)
            location_new = re.sub(r'\[(.*)\]','',location_new)
            location_new = re.sub(r'\s','',location_new)
        if len(location_new):
            item['location'] = location_new
        else:
            item['location'] = ' '
        # item['location'] = location_new


        cate = response.xpath('.').re('<dt class="basicInfo-item name">类.*别</dt>\s<dd class="basicInfo-item value">\s(.+?)\s</dd>')
        # f_name = str(f_name[0])
        # f_name = re.findall(u"[\u4e00-\u9fa5]+",name)
        # lf_name = ''
        # for i in range(len(name)):
        #     m += str(name[i])
        # name = name.decode('utf8')
        # print(cate)
        cate = ''.join(cate)
        cate = str(cate)
        cate = re.sub(r'<\/?.+?\/?>','',cate)
        cate = re.sub(r'\[(.*)\]','',cate)
        cate = re.sub(r'\s','',cate)
        item['category'] = cate

        price = response.xpath('.').re('<dt class="basicInfo-item name">门票价格</dt>\s<dd class="basicInfo-item value">\s(.+?)\s</dd>')
        # f_name = str(f_name[0])
        # f_name = re.findall(u"[\u4e00-\u9fa5]+",name)
        # lf_name = ''
        # for i in range(len(name)):
        #     m += str(name[i])
        # name = name.decode('utf8')
        # print(price)
        price = ''.join(price)
        price = str(price)
        item['price'] = price

        s = ''
        div_list = response.xpath('//*[@class="lemma-summary"]/div//text()').extract()
        for div in div_list:
            # a_list = div.xpath('./a')
            # # print(a_list)
            # for a in a_list:
            s += div
        s = re.sub(r'\[(.*)\]','',s)
        s = re.sub(r'\s','',s)
        # print(s)
        s = ''.join(s)
        item['introduction'] = s
        yield item


        # mus_name = ['中国国家博物馆','上海科技馆','中央苏区（闽西）历史博物馆']
        # print(mus_name)
        for i in range(len(self.mus_name)):
            if i == 0:
                continue
            # self.num += 1
            name = str(self.mus_name[i])
            url_use = self.url + name
            if name == '四川博物院':
                url_use = 'https://baike.baidu.com/item/%E5%9B%9B%E5%B7%9D%E5%8D%9A%E7%89%A9%E9%99%A2/2812558'
            # print(url)
            if name == '郑州博物馆':
                url_use = 'https://baike.baidu.com/item/%E9%83%91%E5%B7%9E%E5%8D%9A%E7%89%A9%E9%A6%86/783622'
            yield scrapy.Request(url_use,callback=self.parse,meta = {'name':name})

