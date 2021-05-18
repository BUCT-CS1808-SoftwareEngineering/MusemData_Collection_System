import scrapy
from selenium import webdriver


class DyjySpider(scrapy.Spider):
    name = 'education192'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.cnfm.org.cn/shjy/dydjt.shtml']

    model_urls = []
    model_urls.append(start_urls[0])

    def __init__(self):
        self.bro = webdriver.Chrome(executable_path = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chromedriver.exe')

    def parse(self, response):
        table_list = response.xpath('//*[@id="2019/09/28/564_1_CMSTitleList.txt"]/table')
        # print(tr_list)
        for i in table_list:
            title = response.xpath('/html/body/table[1]/tbody/tr/td/table[2]/tbody/tr/td/table/tbody/tr[3]/td[2]/table/tbody/tr[1]/td/text()').extract_first()
            img = None
            content = i.xpath('./tbody/tr/td/a/text()').extract_first()
            print(title, img, content)

    def closed(self,spider):
        self.bro.quit()

