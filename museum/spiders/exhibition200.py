import scrapy
from selenium import webdriver

class CiaezlSpider(scrapy.Spider):
    name = 'exhibition200'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.ciae.com.cn/display/zh/civilization.html']

    model_urls = []
    model_urls = start_urls

    def __init__(self):
        self.bro = webdriver.Chrome(executable_path = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chromedriver.exe')

    def parse_detail(self, response):
        content = response.xpath('/html/body/div[3]/div/div/div[2]//text()').extract()
        content = ''.join(content).replace('\n', '').replace('\r', '')

        # content = content[1]
        print(content)

    def parse(self, response):
        li_list = response.xpath('//*[@id="ajax-list"]/ul/li')
        for i in li_list:
            title = i.xpath('./a/div[2]/h3/text()').extract_first()
            img = 'https://www.ciae.com.cn' + i.xpath('./a/div[1]/img/@src').extract_first()
            detail_url = 'https://www.ciae.com.cn' + i.xpath('./a/@href').extract_first()
            print(title, img, detail_url)
            yield scrapy.Request(detail_url, callback=self.parse_detail)
    def closed(self,spider):
        self.bro.quit()
