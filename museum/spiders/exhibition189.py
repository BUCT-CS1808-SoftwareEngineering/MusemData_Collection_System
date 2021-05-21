import scrapy
from selenium import webdriver
from museum.items import exhibitionItem

class TjzrzlSpider(scrapy.Spider):
    name = 'exhibition189'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.tjnhm.com/index.php?p=zlxx&c_id=5&lanmu=2']

    model_urls = start_urls

    def __init__(self):
        self.bro = webdriver.Chrome(executable_path = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chromedriver.exe')

    def parse_detail(self, response):
        p_list = response.xpath('//*[@id="aboutus_text"]//text()').extract()
        content = ''.join(p_list).replace('\r', '').replace('\n', ' ').split('上一条')[0]
        print(content)

    def parse(self, response):
        div_list = response.xpath('//*[@id="news_content"]/div')
        for i in div_list:
            url = 'https://www.tjnhm.com/' + i.xpath('./a[1]/@href').extract_first()
            title = i.xpath('./a[2]/text()').extract_first()
            img = 'https://www.tjnhm.com/' + i.xpath('./a[1]/img/@src').extract_first()
            print(url, img, title)
            yield scrapy.Request(url, callback=self.parse_detail)

    def closed(self,spider):
        self.bro.quit()