import scrapy
from selenium import webdriver
import re

class GmczlSpider(scrapy.Spider):
    name = 'exhibition201'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://gmc.org.cn/exhib/detail/39.html', 'http://gmc.org.cn/exhib/detail/48.html', 'http://gmc.org.cn/exhib/detail/50.html', 'http://gmc.org.cn/exhib/detail/49.html']

    model_urls = []
    model_urls = start_urls

    def __init__(self):
        self.bro = webdriver.Chrome(executable_path = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chromedriver.exe')

    def parse(self, response):
        title = response.xpath('/html/body/div[4]/div/div[1]/div[2]/div/div[1]/text()').extract_first()
        img = "http://gmc.org.cn" + response.xpath('/html/body/div[4]/div/div[1]/div[1]/@style').extract_first().split('("')[1].split('")')[0]
        # img = re.search('(?<=\()\S+(?=\))',img).group()
        content = response.xpath('//*[@id="mCSB_1_container"]//text()').extract()
        content = ''.join(content)
        print(title, img, content)

    def closed(self,spider):
        self.bro.quit()
# background-image: url("/Uploads/Picture/2019/10/08/s5d9c45e86ef75.jpg"); visibility: inherit; opacity: 1; transform: matrix(1, 0, 0, 1, 0, 0);