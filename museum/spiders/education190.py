import scrapy
from selenium import webdriver
from museum.items import educationItem

class ZeljySpider(scrapy.Spider):
    name = 'education190'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.mzhoudeng.com/news.aspx?cateid=92']

    model_urls = start_urls

    def __init__(self):
        self.bro = webdriver.Chrome(executable_path = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chromedriver.exe')

    def parse_detail(self, response):
        item = educationItem()
        title = response.xpath('/html/body/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[1]/text()').extract_first()
        content = response.xpath('/html/body/div[3]/div/div[1]/div[2]/div[2]/div[2]//text()').extract()
        content = ''.join(content)
        img = response.xpath('/html/body/div[3]/div/div[1]/div[2]/div[2]/div[2]/p[1]/img/@src').extract_first()
        if not img.startswith('http://www.mzhoudeng.com/') and img:
            img = 'http://www.mzhoudeng.com/' + img
        if img:
            item['eduName'] = title
            item['eduImg'] = img
            item['eduContent'] = content
        print(title, content, img)

    def parse(self, response):
        li_list = response.xpath('/html/body/div[3]/div/div[1]/div[2]/div[2]/ul/li')
        for i in li_list:
            url = 'http://www.mzhoudeng.com/' + i.xpath('./a/@href').extract_first()
            yield scrapy.Request(url, callback=self.parse_detail)


    def closed(self,spider):
        self.bro.quit()
