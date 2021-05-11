import scrapy
from museum.items import educationItem
#scrapy crawl collection
#scrapy crawl exhiition
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
#scrapy genspider education
class Education9Spider(scrapy.Spider):
    name = 'education131'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.mtybwg.org.cn/xuanjiao/117-1.aspx']

    def parse(self, response):
        item = educationItem()
        #scrapy crawl education131
        div_list = response.xpath('/html/body/div[2]/div[2]/ul/ul/li')
        print(div_list)
        for li in div_list:
            name = li.xpath('./a//text()').extract_first()
            print(name)
            detail_url=li.xpath('./a/@href').extract_first()
            detail_url='http://www.mtybwg.org.cn'+detail_url
            print(detail_url)
            img = 'https://mmbiz.qpic.cn/mmbiz_jpg/coHcbvPjfouGPPDkRweOgvEMZUAMjstjaVcypr3tib4THjr4w0FcQZt6S2YwHfvjDY1vfmVoFTkhsHr6viazRp8Q/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1'
            print(img)
            #cont=response.xpath('/html/body/div[1]/div[2]/div[1]/div/div[1]/div[3]/section/section[5]//text()').extract()
            cont =detail_url
            print(cont)