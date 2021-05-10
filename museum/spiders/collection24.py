import scrapy
from museum.items import collectionItem
import re
from selenium import webdriver
# scrapy crawl collection24

class Collection24Spider(scrapy.Spider):
    name = 'collection24'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.sxgm.org/home/picnews/index/c_id/104/lanmu/61.html',
    'http://www.sxgm.org/home/picnews/index/c_id/105/lanmu/61.html',
    'http://www.sxgm.org/home/picnews/index/c_id/106/lanmu/61.html',
    'http://www.sxgm.org/home/picnews/index/c_id/107/lanmu/61.html',
    'http://www.sxgm.org/home/picnews/index/c_id/108/lanmu/61.html']

    new_urls = ['http://www.sxgm.org/home/picnews/index/c_id/104/lanmu/61.html',
    'http://www.sxgm.org/home/picnews/index/c_id/105/lanmu/61.html',
    'http://www.sxgm.org/home/picnews/index/c_id/106/lanmu/61.html',
    'http://www.sxgm.org/home/picnews/index/c_id/107/lanmu/61.html',
    'http://www.sxgm.org/home/picnews/index/c_id/108/lanmu/61.html']
    deep_urls = []
    # url = 'http://www.zhejiangmuseum.com/Collection/ExcellentCollection?page=%d'
    # page_num = 2

    #实例化一个
    def __init__(self):
        self.bro = webdriver.Firefox()
        self.brom = webdriver.Firefox()

    def parse_detail(self, response):
        item = response.meta["item"]
        coll_name = response.xpath('/html/body/div[5]/div/div[2]/div[4]/table/tbody/tr[1]/td[2]/font/text()').extract_first()
        # coll_name = re.sub('&(.+?);','',coll_name)
        print(coll_name)
        # /html/body/div[5]/div/div[2]/ul/li[1]/a/table/tbody/tr[1]/td/img
        coll_img = response.xpath('/html/body/div[5]/div/div[2]/div[4]/table/tbody/tr[1]/td[1]/div/div[1]//img/@src').extract_first()
        coll_img = 'http://www.sxgm.org' + coll_img
        print(coll_img)
        coll_desc = "暂无介绍"
        if response.xpath('/html/body/div[5]/div/div[2]/div[4]/table/tbody/tr[2]/td/div//text()'):
            coll_desc = response.xpath('/html/body/div[5]/div/div[2]/div[4]/table/tbody/tr[2]/td/div//text()').extract()
            coll_desc = ''.join(coll_desc)
        print(coll_desc)
            
        # yield item

    def parse(self, response):
        item = collectionItem()
        coll_list = response.xpath('/html/body/div[5]/div/div[2]/ul/li')
        for li in coll_list:
            # coll_name = li.xpath('./a/table/tbody/tr[2]/td/div/text()').extract_first()
            # # coll_name = re.sub('&(.+?);','',coll_name)
            # print(coll_name)
            # # /html/body/div[5]/div/div[2]/ul/li[1]/a/table/tbody/tr[1]/td/img
            # coll_img = li.xpath('./a/table/tbody/tr[1]/td/img/@src').extract_first()
            # coll_img = 'http://www.sxgm.org' + coll_img
            # print(coll_img)
            detail_url = "http://www.sxgm.org" + li.xpath('./a/@href').extract_first()
            print(detail_url)
            self.deep_urls.append(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
    
    def closed(self,spider):
        self.bro.quit()
        self.brom.quit()
