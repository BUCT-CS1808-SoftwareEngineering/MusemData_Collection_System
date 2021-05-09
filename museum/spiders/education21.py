import scrapy
from museum.items import educationItem
# scrapy crawl education21

class Education21Spider(scrapy.Spider):
    name = 'education21'
    start_urls = ['http://www.bjqtm.com/xcjy/sjhd/']

    def parse(self, response):
        item = educationItem()
        li_list = response.xpath('/html/body/div[4]/div/div[2]/div[2]/div[1]/ul/li')
        for li in li_list:
            name = li.xpath('./div[2]/h3/text()').extract()
            name = ''.join(name)
            print(name)
            # item['exhibName'] = name          
            # item['exhibImg'] = img
            detail_url = li.xpath('./a/@href').extract_first()
            detail_url = 'http://www.bjqtm.com' + detail_url
            # print(detail_url)
            yield scrapy.Request(url=detail_url,callback=self.parse_detail)
    
    def parse_detail(self, response):
        img = response.xpath('/html/body/div[4]/div/div[2]/div[2]/div[1]//img/@src').extract_first()
        img = ''.join(img)
        img = 'http://www.bjqtm.com' + img
        print(img)
        cont = response.xpath('/html/body/div[4]/div/div[2]/div[2]/div[1]//text()').extract()
        cont = ''.join(cont)
        # time = response.xpath('/html/body/div[3]/div[2]/div/ul[2]/li[2]/span[2]/text()').extract()
        # time = ''.join(time)
        # loca = response.xpath('/html/body/div[3]/div[2]/div/ul[2]/li[2]/span[4]/text()').extract()
        # loca = ''.join(loca)
        # time = response.xpath('//*[@id="app"]/div/div/div/div/main/div[1]/div[3]/div[2]/div[1]/div[1]/p/text()').extract()
        # time = ''.join(time)
        # loca = response.xpath('//*[@id="app"]/div/div/div/div/main/div[1]/div[3]/div[2]/div[1]/div[2]/p/text()').extract()
        # loca = ''.join(loca)
        # cont = cont + '\n展览时间：' + time + '\n展览地点：' + loca
        print(cont)