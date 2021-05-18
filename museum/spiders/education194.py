import scrapy
from selenium import webdriver

class TwjySpider(scrapy.Spider):
    name = 'education194'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.bjp.org.cn/kphd/yzsnt/index.shtml']

    model_urls = []
    model_urls = start_urls

    def __init__(self):
        self.bro = webdriver.Chrome(executable_path = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chromedriver.exe')

    def parse_detail(self, response):
        try:
            name = response.xpath('/html/body/div[3]/div[2]/div[2]/div[2]/div[1]/p/span/text()').extract_first()
            img = 'http://www.bjp.org.cn' + response.xpath('/html/body/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div/div/div/img[2]/@src |'
                                                           '/html/body/div[3]/div/ul/li/div/div[1]/div/div/img[2]/@src').extract_first()
            content = response.xpath('/html/body/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]//text()').extract()
            content = ''.join(content).replace('\n', '')

            print(name, img, content)
        except:
            pass


    def parse(self, response):
        li_list = response.xpath('/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/ul/li')
        for i in li_list:
            detail_url = 'http://www.bjp.org.cn' + i.xpath('./a/@href').extract_first()
            yield scrapy.Request(detail_url, callback=self.parse_detail)

    def closed(self,spider):
        self.bro.quit()