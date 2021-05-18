import scrapy
from selenium import webdriver

class ZelzlSpider(scrapy.Spider):
    name = 'exhibition190'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.mzhoudeng.com/exhibits.aspx?cateid=88']

    # url = 'http://www.mzhoudeng.com/relics.aspx?cateid=89&page={}'
    # for i in range(1, 8):
    #     start_urls.append(url.format(i))
    # # print(start_urls)

    model_urls = start_urls

    def __init__(self):
        self.bro = webdriver.Chrome(executable_path = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chromedriver.exe')

    def parse_detail(self, response):
        content = response.xpath('/html/body/div[3]/div/div[1]/div[2]/div[2]/div[3]//text()').extract()
        content = ''.join(content)
        print(content)




    def parse(self, response):
        li_list = response.xpath('/html/body/div[3]/div/div[1]/div[2]/div[2]/ul/li')
        for i in li_list:
            detail_url = 'http://www.mzhoudeng.com/' + i.xpath('./a/@href').extract_first()
            img = 'http://www.mzhoudeng.com/' + i.xpath('./a/img/@src').extract_first()
            title = i.xpath('./a/div/div[1]/text()').extract_first()
            print(detail_url, img, title)
            yield scrapy.Request(detail_url, callback=self.parse_detail)




    def closed(self,spider):
        self.bro.quit()

