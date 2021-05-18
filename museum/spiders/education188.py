import scrapy
from museum.items import educationItem
import re 
# scrapy crawl education188

class Education188Spider(scrapy.Spider):
    name = 'education188'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://pjcmm.com/listNews.aspx?cateid=87']

    def parse(self, response):
        item = educationItem()
        li_list = response.xpath('//ul[@class="listNews"]/li')
        num = 1
        for li in li_list:
            if num > 6:
                break
            name = li.xpath('./a/text()').extract_first()
            # name = ''.join(name)
            # name = re.sub('&(.+?);','',name)
            print(name)
            # item['exhibName'] = name          
            # item['exhibImg'] = img
            # //*[@id="body_wrap"]/div/div[2]/div[2]/div[2]/dl[1]/
            
            detail_url = "http://pjcmm.com/" + li.xpath('./a/@href').extract_first()
            print(detail_url)
            # //*[@id="body_wrap"]/div/div[2]/div[2]/div[2]/dl[1]/
            # cont = li.xpath('./dt/span/text()').extract_first()
            # print(cont)
            yield scrapy.Request(url=detail_url,callback=self.parse_detail,meta={'item':item})
    
    def parse_detail(self, response):
        item = response.meta["item"]
        img = "http://pjcmm.com" + response.xpath('/html/body/div[4]/div[2]/p//img/@src').extract_first()
        # img = 'http://www.njiemuseum.com' + img
        print(img)
        cont = response.xpath('/html/body/div[4]/div[2]/p//text()').extract()
        cont = ''.join(cont)
        # cont = re.sub('【\d】','',cont)
        print(cont)
