import scrapy
from selenium import webdriver

class GmcSpider(scrapy.Spider):
    name = 'collection201'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://gmc.org.cn/mineral.html','http://gmc.org.cn/fossil.html','http://gmc.org.cn/gemandjade.html','http://gmc.org.cn/other.html']

    model_urls = []
    model_urls = start_urls

    def __init__(self):
        self.bro = webdriver.Chrome(executable_path = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chromedriver.exe')

    def parse_d(self, response):
        content = response.xpath('//*[@id="mCSB_1_container"]/div//text()').extract()
        # print(content)
        content = ''.join(content)
        print(content)

    def parse(self, response):
        # title = response.xpath('/html/body/div[4]/div/div/div[4]/div/div[1]/div[1]/div/a/div[2]/text() | '
        # title = response.xpath('/html/body/div[4]/div/div/div[4]/div/div[1]/div[2]/div/a/div[2]/div[1]/text() |'
        #                        '//*[@id="datalist"]/div[1]/div[1]/a/div[2]/text() |'
        #                        '//*[@id="datalist"]/div[1]/div[2]/a/div[2]/text() |'
        #                        '//*[@id="datalist"]/div[1]/div[3]/a/div[2]/text() |'
        #                        '//*[@id="datalist"]/div[1]/div[4]/a/div[2]/text() |'
        #                        '//*[@id="datalist"]/div[1]/div[5]/a/div[2]/text() |'
        #                        '//*[@id="datalist"]/div[1]/div[6]/a/div[2]/text() |'
        #                        '//*[@id="datalist"]/div[1]/div[7]/a/div[2]/text() |'
        #                        '//*[@id="datalist"]/div[1]/div[8]/a/div[2]/text()').extract_first()
        # img = 'http://gmc.org.cn' + response.xpath('/html/body/div[4]/div/div/div[4]/div/div[1]/div[1]/div/a/img/@src | '
        #                                            '/html/body/div[4]/div/div/div[4]/div/div[1]/div[2]/div/a/div[1]/img/@src |'
        #                                            '//*[@id="datalist"]/div[1]/div[1]/a/img/@src |'
        #                                            '//*[@id="datalist"]/div[1]/div[2]/a/img/@src |'
        #                                            '//*[@id="datalist"]/div[1]/div[3]/a/img/@src |'
        #                                            '//*[@id="datalist"]/div[1]/div[4]/a/img/@src |'
        #                                            '//*[@id="datalist"]/div[1]/div[5]/a/img/@src |'
        #                                            '//*[@id="datalist"]/div[1]/div[6]/a/img/@src |'
        #                                            '//*[@id="datalist"]/div[1]/div[7]/a/img/@src |'
        #                                            '//*[@id="datalist"]/div[1]/div[8]/a/img/@src').extract_first()
        # detail_url = 'http://gmc.org.cn' + response.xpath('/html/body/div[4]/div/div/div[4]/div/div[1]/div[1]/div/a/@href | '
        #                                                   '/html/body/div[4]/div/div/div[4]/div/div[1]/div[2]/div/a/@href |'
        #                                                   '//*[@id="datalist"]/div[1]/div[1]/a/@href |'
        #                                                   '//*[@id="datalist"]/div[1]/div[2]/a/@href |'
        #                                                   '//*[@id="datalist"]/div[1]/div[3]/a/@href |'
        #                                                   '//*[@id="datalist"]/div[1]/div[4]/a/@href |'
        #                                                   '//*[@id="datalist"]/div[1]/div[5]/a/@href |'
        #                                                   '//*[@id="datalist"]/div[1]/div[6]/a/@href |'
        #                                                   '//*[@id="datalist"]/div[1]/div[7]/a/@href |'
        #                                                   '//*[@id="datalist"]/div[1]/div[8]/a/@href').extract_first()
        div_list = response.xpath('//*[@id="datalist"]/div[1]/div')
        for i in div_list:
            title = i.xpath('./a/div[2]/text()').extract_first()
            img = 'http://gmc.org.cn' + i.xpath('./a/img/@src').extract_first()
            detail_url = 'http://gmc.org.cn' + i.xpath('./a/@href').extract_first()
            print(title, img, detail_url)
            self.model_urls.append(detail_url)
            yield scrapy.Request(detail_url, callback=self.parse_d)

    def closed(self,spider):
        self.bro.quit()