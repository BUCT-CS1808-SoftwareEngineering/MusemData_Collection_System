import scrapy
from selenium import webdriver
from museum.items import educationItem
# scrapy crawl education36

class Education36Spider(scrapy.Spider):
    name = 'education36'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.tssbwg.com.cn/index.php?m=content&c=index&a=lists&catid=35']

    new_urls = ['http://www.tssbwg.com.cn/index.php?m=content&c=index&a=lists&catid=35']
    deep_urls = []

    #实例化一个
    def __init__(self):
        self.bro = webdriver.Firefox()
        self.brom = webdriver.Firefox()

    def parse(self, response):
        item = educationItem()
        li_list = response.xpath('/html/body/table[2]/tbody/tr/td[1]/div/table[3]/tbody/tr/td/ul/table')
        num = 1
        for li in li_list:
            if num > 6:
                break
            num += 1
            name = li.xpath('./tbody/tr[1]/td[1]/div/a/text()').extract()
            name = ''.join(name)
            print(name)
            detail_url = li.xpath('./tbody/tr[1]/td[1]/div/a/@href').extract_first()
            print(detail_url)
            self.deep_urls.append(detail_url)
            
            yield scrapy.Request(url=detail_url,callback=self.parse_detail)
    
    def parse_detail(self, response):
        img = response.xpath('/html/body/table[2]/tbody/tr/td/div/table[6]/tbody/tr/td//img/@src').extract_first()
        # img = ''.join(img)
        # img = 'https://activity.wisdommuseum.cn' + img
        print(img)
        cont = "暂无"
        if response.xpath('/html/body/table[2]/tbody/tr/td/div/table[6]/tbody/tr/td//text()').extract():
            cont = response.xpath('/html/body/table[2]/tbody/tr/td/div/table[6]/tbody/tr/td//text()').extract()
            cont = ''.join(cont)
        print(cont)

    def closed(self,spider):
        self.bro.quit()
        self.brom.quit()