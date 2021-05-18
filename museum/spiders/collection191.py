import scrapy
from selenium import webdriver

class AutoSpider(scrapy.Spider):
    name = 'collection191'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.automuseum.org.cn/ZLJS/CPJX/list-cpjx1.html?/ZLJS/CSZL/']
    url = 'http://www.automuseum.org.cn/ZLJS/CPJX/list-cpjx{}.html?/ZLJS/CSZL/'
    for i in range(2, 19):
        start_urls.append(url.format(i))
    model_urls = []
    model_urls = start_urls

    def __init__(self):
        self.bro = webdriver.Chrome(executable_path = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chromedriver.exe')


    def parse(self, response):
        title = response.xpath('/html/body/div[2]/div[2]/div[2]/div/table/tbody/tr/td[3]/table/tbody/tr[1]/td/div/span/strong/text() |'
                               ' /html/body/div[2]/div[2]/div[2]/div/table/tbody/tr/td[3]/table/tbody/tr[1]/td/div/strong/text() |'
                               '/html/body/div[2]/div[2]/div[2]/div/table/tbody/tr/td[3]/table/tbody/tr[1]/td/div/p[2]/strong/text()').extract_first()
        img = 'http://www.automuseum.org.cn' + response.xpath('/html/body/div[2]/div[2]/div[2]/div/table/tbody/tr/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/div/img/@src').extract_first()
        content = response.xpath('/html/body/div[2]/div[2]/div[2]/div/table/tbody/tr/td[3]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/text()').extract()
        content = ''.join(content).replace('\n', '')
        print(title, img, content)

    def closed(self,spider):
        self.bro.quit()