import scrapy
from museum.items import educationItem
import re 
# scrapy crawl education26

class Education26Spider(scrapy.Spider):
    name = 'education26'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.njiemuseum.com/index.php/Index/Index/col/c_id/63.html']

    def parse(self, response):
        item = educationItem()
        li_list = response.xpath('//*[@id="ContentPlaceHolder1_main_cnt"]/ul/li')
        num = 1
        for li in li_list:
            if num > 6:
                break
            name = li.xpath('./div/div[2]/a[1]/h1/text()').extract_first()
            # name = ''.join(name)
            # name = re.sub('&(.+?);','',name)
            print(name)
            # item['exhibName'] = name          
            # item['exhibImg'] = img
            img = li.xpath('./div/div[1]/img/@src').extract_first()
            img = 'http://www.njiemuseum.com' + img
            print(img)
            detail_url = "http://www.njiemuseum.com" + li.xpath('./div/div[2]/a[1]/@href').extract_first()
            print(detail_url)
            yield scrapy.Request(url=detail_url,callback=self.parse_detail,meta={'item':item})
    
    def parse_detail(self, response):
        item = response.meta["item"]
        cont = response.xpath('//*[@id="ContentPlaceHolder1_cnt"]/div/div/div[5]//text()').extract()
        cont = ''.join(cont)
        # cont = re.sub('【\d】','',cont)
        print(cont)

