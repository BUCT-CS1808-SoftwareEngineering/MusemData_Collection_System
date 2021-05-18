import scrapy
from selenium import webdriver

class AutozlSpider(scrapy.Spider):
    name = 'exhibition191'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.automuseum.org.cn/ZLJS/CSZL/CZG/news-lsdcl.html',
                  'http://www.automuseum.org.cn/ZLJS/CSZL/JBG/news-jgqc.html',
                  'http://www.automuseum.org.cn/ZLJS/CSZL/WLG/news-qczm.html']
    model_urls = []
    model_urls = start_urls

    def __init__(self):
        self.bro = webdriver.Chrome(executable_path = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chromedriver.exe')


    def parse(self, response):
        title = response.xpath('/html/body/div[2]/div[2]/div[2]/table/tbody/tr[2]/td/div/strong/text() | '
                               '/html/body/div[2]/div[2]/div[2]/table/tbody/tr[2]/td/div/strong/text() |'
                               '/html/body/div[2]/div[2]/div[2]/table/tbody/tr[2]/td/div/strong/text()').extract_first()
        img = 'http://www.automuseum.org.cn' + response.xpath('/html/body/div[2]/div[2]/div[2]/table/tbody/tr[3]/td/div/img/@src |'
                                                              '/html/body/div[2]/div[2]/div[2]/table/tbody/tr[3]/td[1]/img/@src |'
                                                              '/html/body/div[2]/div[2]/div[2]/table/tbody/tr[3]/td/div/img/@src').extract_first()
        content = response.xpath('/html/body/div[2]/div[2]/div[2]/table/tbody/tr[3]/td[2]/p/span/text() |'
                                 '/html/body/div[2]/div[2]/div[2]/table/tbody/tr[4]/td/span//text() |'
                                 '/html/body/div[2]/div[2]/div[2]/table/tbody/tr[4]/td/p/text()').extract()
        content = ''.join(content).replace('\n', '')
        print(title, img, content)

    def closed(self,spider):
        self.bro.quit()