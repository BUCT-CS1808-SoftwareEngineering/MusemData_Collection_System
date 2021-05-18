import scrapy
from selenium import webdriver

class DySpider(scrapy.Spider):
    name = 'collection192'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.cnfm.org.cn/gcjp/gcjp.shtml']
    model_urls = []
    model_urls.append(start_urls[0])

    def __init__(self):
        self.bro = webdriver.Chrome(executable_path = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chromedriver.exe')

    def parse(self, response):
        tr_list = response.xpath('/html/body/table[1]/tbody/tr/td/table[2]/tbody/tr/td/table/tbody/tr[3]/td[2]/table/tbody/tr/td/table/tbody/tr')
        # print(tr_list)
        for i in tr_list:
            td_list = i.xpath('./td')
            for j in td_list:
                title = j.xpath('./div/p/a/text()').extract_first()
                # print(j.xpath('./div'))
                img = 'http://www.cnfm.org.cn' + j.xpath('./div/a/img/@src').extract_first()
                print(title, img)
    def closed(self,spider):
        self.bro.quit()