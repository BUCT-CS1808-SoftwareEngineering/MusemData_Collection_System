import scrapy
from selenium import webdriver

class AutojySpider(scrapy.Spider):
    name = 'education191'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.automuseum.org.cn/list_2.html?/KPJY/KPKT/']

    model_urls = []
    model_urls = start_urls

    def __init__(self):
        self.bro = webdriver.Chrome(executable_path = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chromedriver.exe')

    def parse_detail(self, response):
        title = response.xpath('/html/body/div[2]/div[2]/span/div[1]/span/text()').extract_first() + response.xpath('//*[@id="detail"]/p[2]/span/text()').extract_first()
        img = response.xpath('//*[@id="detail"]/p[1]/span/img/@src').extract_first()
        content = response.xpath('//*[@id="detail"]/p[3]/span//text()').extract()
        content = ''.join(content)
        print(title, img, content)

    def parse(self, response):
        dl_list = response.xpath('//*[@id="page1 "]/ul/dl')
        print(dl_list)
        for i in dl_list:
            title = i.xpath('./dt/a/text()').extract_first()
            print(title)
            if '双语科普' in title:
                detail_url = 'http://www.automuseum.org.cn' + i.xpath('./dt/a/@href').extract_first()
                self.model_urls.append(detail_url)
                yield scrapy.Request(detail_url, callback=self.parse_detail)


    def closed(self,spider):
        self.bro.quit()
