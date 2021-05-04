import scrapy
from museum.items import educationItem
import requests
import re
from lxml import etree
#scrapy crawl education4

class Education4Spider(scrapy.Spider):
    name = 'education4'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://cstm.cdstm.cn/jyhd/zkgdjt/']

    def parse_detail(self, response):
        item = response.meta["item"]
        # url = response.meta["url"]
        name = response.xpath('/html/body/div[4]/div[3]/div[2]/div/h2/text()').extract_first()
        # name = ''.join(name)
        print(name)
        #<p><strong>讲座提纲：</strong></p>\s([\s\S]*?)\s<p>
        content = response.xpath('/html/body/div[4]/div[3]/div[2]/div/div[1]//text()').extract()
        # content = 
        content = ''.join(content)
        # res = requests.get(url)
        # ahtml = etree.HTML(res.text)
        # print(ahtml)
        # content = response.xpath('.')
        # content = response.xpath('.').re('<li><a href="../../">(.+?)</a></li>')
        # content = response.xpath('/html/body/div[4]/div[3]/div[2]/div/div[1]').re('<p style="padding: 5px 0px; margin-right: 0px; margin-left: 0px; font-size: 14px; line-height: 21px; text-indent: 2em; font-family: &quot;Microsoft Yahei&quot;, STHeiti, 宋体, simsun, &quot;Arial Narrow&quot;, 宋体, arial, Arial, sans-serif;"><strong><span style="font-size: 16px; line-height: 24px; font-family: 黑体;">【内容提要】</span></strong></p>[\s\S]*</div>')
        # content = str(content)
        # content = re.sub(r'<\/?.+?\/?>','',content)
        # content = ''.join(content)
        print(content)

    def parse(self, response):
        item = educationItem()
        div_list = response.xpath('/html/body/div[4]/div[3]/div[2]/div/div[2]/div/div[@class="jchg-cont"]')
        # print(div_list)
        # //*[@id="hd1-4"]/div[2]/div/div[1]/div/div[4]/div[2]/a/h2
        for div in div_list:
            img = str(div.xpath('./a/img/@src').extract_first())
            img = img.replace(img[0],'',1)
            img = "https://cstm.cdstm.cn/jyhd/zkgdjt" + img
            print(img)
            # name = div.xpath('./div[2]/a/h2/text()').extract_first()
            # print(name)
            url = str(div.xpath('./a/@href').extract_first())
            url = url.replace(url[0],'',1)
            # print(url)
            url_use = "https://cstm.cdstm.cn/jyhd/zkgdjt" + url
            # print(url_use)
            yield scrapy.Request(url_use,callback=self.parse_detail,meta={'item':item,'url':url_use})