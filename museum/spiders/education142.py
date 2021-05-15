import scrapy
from museum.items import educationItem
#scrapy crawl collection
#scrapy crawl exhiition
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
#scrapy genspider education
class Education9Spider(scrapy.Spider):
    name = 'education142'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.nanhujng.com/xjzc/zthd/']

    def parse(self, response):
        item = educationItem()
        #scrapy crawl education142
        div_list = response.xpath('/html/body/div[6]/div[1]/div[2]/div[2]/ul/li')
        for li in div_list:
            name = li.xpath('./a/text()').extract_first()
            print(name)
            detail_url=li.xpath('./a/@href').extract_first()
            detail_url='https://www.nanhujng.com/xjzc/zthd/'+detail_url[1:len(detail_url)]
            print(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
    def parse_detail(self, response):
        item = response.meta["item"]
        img = response.xpath('//*[@class="content_box"]//img/@src').extract_first()
        if(img):
            img='https://www.nanhujng.com/xjzc/zthd/202101/'+img[1:len(img)]
        print(img)
        cont=response.xpath('//*[@class="content_box"]//text()').extract()
        cont = ''.join(cont)
        print(cont)