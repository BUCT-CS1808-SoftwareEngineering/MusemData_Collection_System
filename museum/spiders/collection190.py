import scrapy
from selenium import webdriver

class ZelSpider(scrapy.Spider):
    name = 'collection190'
    # allowed_domains = ['www.xxx.com']
    start_urls = []
    url = 'http://www.mzhoudeng.com/relics.aspx?cateid=89&page={}'
    for i in range(1, 8):
        start_urls.append(url.format(i))
    # print(start_urls)

    model_urls = start_urls

    def __init__(self):
        self.bro = webdriver.Chrome(executable_path = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chromedriver.exe')

    def parse_detail(self, response):
        title = response.xpath('/html/body/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[1]/text()').extract_first()
        img = 'http://www.mzhoudeng.com' + response.xpath('//*[@id="ban_pic1"]/ul/li/a/img/@src').extract_first()
        content = response.xpath('/html/body/div[3]/div/div[1]/div[2]/div[2]/div[3]//text()').extract()
        content = ''.join(content)
        print(title, img, content)




    def parse(self, response):
        li_list = response.xpath('/html/body/div[3]/div/div[1]/div[2]/div[2]/ul/li')
        for i in li_list:
            detail_url = 'http://www.mzhoudeng.com/' + i.xpath('./a/@href').extract_first()
            self.model_urls.append(detail_url)
            # print(detail_url)
            yield scrapy.Request(detail_url, callback=self.parse_detail)



    def closed(self,spider):
        self.bro.quit()


# http://www.mzhoudeng.com/relicsin.aspx?cateid=89&Productsid=156