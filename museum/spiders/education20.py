import scrapy
from museum.items import educationItem
# scrapy crawl education20

class Education20Spider(scrapy.Spider):
    name = 'education20'
    start_urls = ['http://www.gansumuseum.com/xsyj/list-65.html']

    def parse(self, response):
        item = educationItem()
        li_list = response.xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/ul/li')
        for li in li_list:
            name = li.xpath('./div/a[2]/div/div[1]/label/text()').extract()
            name = ''.join(name)
            print(name)
            # item['exhibName'] = name          
            # item['exhibImg'] = img
            img = li.xpath('./div/a[1]/img/@src').extract()
            img = ''.join(img)
            img = 'http://www.gansumuseum.com' + img
            print(img)
            cont = li.xpath('./div/a[2]/div/div[2]/p/text()').extract()
            cont = ''.join(cont)
            print(cont)
            # yield scrapy.Request(url=detail_url,callback=self.parse_detail)
