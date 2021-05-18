# -*- coding: utf-8 -*-
import scrapy
from njmusePro.get_suburl import getsub

class BjzrSpider(scrapy.Spider):
    name = 'collection198'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.bmnh.org.cn/gzxx/gzbb/1/list.shtml']
    url = 'http://www.bmnh.org.cn/gzxx/gzbb/{}/list.shtml'
    # class_list = [2,3,4,5,6,7,14,8,10,9,12,13,11]
    for i in range(2, 16):
        start_urls.append(url.format(i))
    # print(start_urls)

    def parse(self, response):
        div_list = response.xpath('/html/body/div[3]/div[3]/div[2]/div[1]/div')
        path1 = '/html/body/div[3]/div[3]/div[2]/div[1]/div[{}]/div/a/img/@src'
        path2 = '/html/body/div[3]/div[3]/div[2]/div[1]/div[{}]/div/a/img/@alt'
        for i in range(1, len(div_list)+1):
            img = 'http://www.bmnh.org.cn' + response.xpath(path1.format(i)).extract_first()
            name = response.xpath(path2.format(i)).extract_first()
            print(img, name)
        url = getsub(response.url)
        # print(url)
        # print(response.xpath('/html/body/div[3]/div[3]/div[2]/div[2]/ul/a[3]/@href').extract_first())
        if response.xpath('/html/body/div[3]/div[3]/div[2]/div[2]/ul/a[3]/@href'):
            next_page = url + response.xpath('/html/body/div[3]/div[3]/div[2]/div[2]/ul/a[3]/@href').extract_first()
            yield scrapy.Request(next_page, callback=self.parse)