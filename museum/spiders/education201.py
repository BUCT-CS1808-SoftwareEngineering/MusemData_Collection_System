import scrapy
from selenium import webdriver

class GmcjySpider(scrapy.Spider):
    name = 'education201'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://gmc.org.cn/lecture.html', 'http://gmc.org.cn/knowledge.html']

    model_urls = []
    model_urls = start_urls

    def __init__(self):
        self.bro = webdriver.Chrome(executable_path = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chromedriver.exe')

    def parse_detail(self, response):
        try:
            img = 'http://gmc.org.cn' + response.xpath('/html/body/div[4]/div/div/div[2]/h5[1]/img/@src |'
                                                       ' /html/body/div[4]/div/div/div[2]/p[4]/img/@src |'
                                                       '/html/body/div[4]/div/div/div[2]/p[5]/img/@src |'
                                                       '/html/body/div[4]/div/div/div[2]/h5[2]/img/@src |'
                                                       '/html/body/div[4]/div/div/div[2]/p[11]/img/@src').extract_first()
            print(img)
        except:
            img = response.xpath('/html/body/div[4]/div/div/div[2]/p[3]/img/@href').extract_first()
            print(img)

    def parse(self, response):
        div_list = response.xpath('//*[@id="datalist"]/div/div')
        for i in div_list:
            detail_url = 'http://gmc.org.cn' + i.xpath('./a/@href').extract_first()
            title = i.xpath('./a/div[1]/div[1]/text()').extract_first()
            content = i.xpath('./a/div[1]/div[3]/text()').extract_first()
            print(detail_url, title, content)
            yield scrapy.Request(detail_url, callback=self.parse_detail)

    def closed(self,spider):
        self.bro.quit()
