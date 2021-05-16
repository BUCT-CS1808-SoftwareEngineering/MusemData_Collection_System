import scrapy
from museum.items import educationItem
#scrapy crawl collection
#scrapy crawl exhiition
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
#scrapy genspider education
class Education9Spider(scrapy.Spider):
    name = 'exhibition158'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.yzmuseum.com/website/exhibition/basic.php?id=141']

    def parse(self, response):
        item = educationItem()
        #scrapy crawl exhibition158
        div_list = response.xpath('//*[@id="content_head"]/div')
        for li in div_list:
            name = li.xpath('./a/text()').extract_first()
            print(name)
            detail_url=li.xpath('./a/@href').extract_first()
            if detail_url:
                detail_url='https://www.yzmuseum.com/'+detail_url
            else: detail_url='https://www.yzmuseum.com/website/exhibition/basic.php?id=141'
            print(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
    def parse_detail(self, response):
        item = response.meta["item"]
        img = response.xpath('//*[@class="pic_area"]//@style').extract_first()
        img=img[22:(len(img)-1)]
        img='https://www.yzmuseum.com/'+img
        print(img)
        cont=response.xpath('//*[@class="content_text"]//text()').extract()
        cont = ''.join(cont)
        print(cont)