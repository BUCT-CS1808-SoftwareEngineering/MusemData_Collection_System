import scrapy
from museum.items import educationItem
import re 
# scrapy crawl education24

class Education24Spider(scrapy.Spider):
    name = 'education24'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.sxgm.org/home/news/index/c_id/99/lanmu/60.html']

    def parse(self, response):
        item = educationItem()
        li_list = response.xpath('/html/body/div[5]/div/div[2]/ul/li')
        # li_list1 = response.xpath('/html/body/div[5]/div/div[2]/ul/li[1]/a/span/text()').extract_first()
        # print(li_list1)
        for li in li_list:
            # /html/body/div[5]/div/div[2]/ul/li[1]/a/span
            name = li.xpath('./a/span/text()').extract_first()
            # name = ''.join(name)
            # name = re.sub('&(.+?);','',name)
            print(name)
            # item['exhibName'] = name          
            # item['exhibImg'] = img
            # img = li.xpath('./img/@src').extract_first()
            # img = 'http://www.nanhaimuseum.org' + img
            # print(img)
            detail_url = "http://www.sxgm.org" + li.xpath('./a/@href').extract_first()
            print(detail_url)
            yield scrapy.Request(url=detail_url,callback=self.parse_detail,meta={'item':item})
    
    def parse_detail(self, response):
        item = response.meta["item"]
        cont = response.xpath('//div[@class="news_detail_content"]/p[1]//text()').extract()
        cont = ''.join(cont)
        # cont = re.sub('【\d】','',cont)
        print(cont)
