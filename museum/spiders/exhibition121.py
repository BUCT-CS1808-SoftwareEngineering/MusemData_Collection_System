import scrapy
from museum.items import exhibitionItem

class ExhibitionSpider(scrapy.Spider):
    name = 'exhibition121'
   # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.zgtcbwg.com/index.php?s=/Home/Article/lists/category/cszl.html']
    def parse_detail(self, response):
        item = response.meta["item"]
        exhib_time ='常设'
        y=response.xpath('/html/body/div[1]/div/div[2]/div[2]//span/text()').extract()
        exhib_intro=''
        for txt in y:
            exhib_intro+=txt
        print(exhib_intro)
    def parse(self, response):
        item = exhibitionItem()
        div_list=response.xpath('/html/body/div[1]/div/div[2]/div[2]/div')
        for div in div_list:
            if(div.xpath('./div[2]/h4/text()').extract_first()!=None):
                exhib_name=div.xpath('./div[2]/h4/text()').extract_first()
                print(exhib_name)
                exhib_location = div.xpath('./div[2]/p[1]/text()').extract_first()
                x=exhib_location[5:len(exhib_location)]
                detail_url = 'http://www.zgtcbwg.com/' + div.xpath('./div[2]//a/@href').extract_first()
                #print(detail_url)
                exhib_location=x
                print(exhib_location)
                yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})


