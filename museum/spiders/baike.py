import scrapy
import re

class BaikeSpider(scrapy.Spider):
    name = 'baike'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://baike.baidu.com/item/%E5%8C%97%E4%BA%AC%E6%95%85%E5%AE%AB%E5%8D%9A%E7%89%A9%E9%99%A2/8663390?fromtitle=%E6%95%85%E5%AE%AB%E5%8D%9A%E7%89%A9%E9%99%A2&fromid=5317',
    'https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E5%9B%BD%E5%AE%B6%E5%8D%9A%E7%89%A9%E9%A6%86'
    ]
    # start_urls = ['https://baike.baidu.com/item/%E5%8C%97%E4%BA%AC%E6%95%85%E5%AE%AB%E5%8D%9A%E7%89%A9%E9%99%A2/8663390?fromtitle=%E6%95%85%E5%AE%AB%E5%8D%9A%E7%89%A9%E9%99%A2&fromid=5317'
    # ]

    def parse(self, response):
        name1 = response.xpath('.').re('<dt class="basicInfo-item name">中文名</dt>\s<dd class="basicInfo-item value">\s(.+?)\s</dd>')
        name1 = str(name1)
        name1 = re.findall(u"[\u4e00-\u9fa5]+",name1)
        m = ''
        for i in range(len(name1)):
            m += str(name1[i])
        # name = name.decode('utf8')
        # print(m)

        # name = response.xpath('.').re('<dt class="basicInfo-item name">外文名</dt>\s<dd class="basicInfo-item value">\s(.+?)\s</dd>')
        # name = str(name)
        # name = re.findall(u"[\u4e00-\u9fa5]+",name)
        # l_name = ''
        # for i in range(len(name)):
        #     m += str(name[i])
        # # name = name.decode('utf8')
        # print(m)

        f_name = response.xpath('.').re('<dt class="basicInfo-item name">外文名</dt>\s<dd class="basicInfo-item value">\s(.+?)\s</dd>')
        f_name = str(f_name[0])
        # f_name = re.findall(u"[\u4e00-\u9fa5]+",name)
        # lf_name = ''
        # for i in range(len(name)):
        #     m += str(name[i])
        # name = name.decode('utf8')
        # print(f_name)


        time = response.xpath('.').re('<dt class="basicInfo-item name">开放时间</dt>\s<dd class="basicInfo-item value">\s([\s\S]*?)\s</dd>')
        time = str(time)
        # time = re.sub('<\/?[\s\S]+?\/?>','',time)
        time = re.sub(r'<(\S*)[^>]*>[^<]*<\/(\1)>','',time)
        print(time)

        cate = response.xpath('.').re('<dt class="basicInfo-item name">类.*别</dt>\s<dd class="basicInfo-item value">\s(.+?)\s</dd>')
        # f_name = str(f_name[0])
        # f_name = re.findall(u"[\u4e00-\u9fa5]+",name)
        # lf_name = ''
        # for i in range(len(name)):
        #     m += str(name[i])
        # name = name.decode('utf8')
        print(cate)

        price = response.xpath('.').re('<dt class="basicInfo-item name">门票价格</dt>\s<dd class="basicInfo-item value">\s(.+?)\s</dd>')
        # f_name = str(f_name[0])
        # f_name = re.findall(u"[\u4e00-\u9fa5]+",name)
        # lf_name = ''
        # for i in range(len(name)):
        #     m += str(name[i])
        # name = name.decode('utf8')
        # print(price)

        s = ''
        div_list = response.xpath('//*[@class="lemma-summary"]/div//text()').extract()
        for div in div_list:
            # a_list = div.xpath('./a')
            # # print(a_list)
            # for a in a_list:
            s += div
        # print(s)