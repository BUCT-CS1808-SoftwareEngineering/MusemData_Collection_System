import scrapy
from selenium import webdriver

class TwSpider(scrapy.Spider):
    name = 'exhibition194'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.bjp.org.cn/cgzn/twzl/list.shtml']

    model_urls = []
    model_urls = start_urls

    def __init__(self):
        self.bro = webdriver.Chrome(executable_path = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chromedriver.exe')

    def parse_detail(self, response):
        pass

    def parse(self, response):
        div_list = response.xpath('//*[@id="zpjs1_1"]/div/div/div')
        div_list.pop()
        for i in div_list:
            name = i.xpath('./div[1]/h2/text()').extract_first()
            img = 'http://www.bjp.org.cn' + i.xpath('./img/@src').extract_first()
            content = i.xpath('./div[2]/p/text()').extract_first()
            print(name, img, content)




    def closed(self,spider):
        self.bro.quit()