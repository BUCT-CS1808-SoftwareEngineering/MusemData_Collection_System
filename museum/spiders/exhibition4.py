import scrapy
from museum.items import exhibitionItem 
import re
# scrapy crawl exhibition4
class Exhibition4Spider(scrapy.Spider):
    name = 'exhibition4'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://cstm.cdstm.cn/cszl/cszljs/']
    new_urls = []
    deep_urls = []
    js1_urls = []
    js2_urls = []
    js3_urls = []
    num = 1

    def parse_detail(self, response):
        item = response.meta["item"]
        item['museumID'] = 4
        divp = response.xpath('/html/body/div[4]/div[3]/div[2]/div/div/p')
        exhib_intro = ''
        for p in divp:
            text = p.xpath('./text()').extract_first()
            if text != None:
                exhib_intro = exhib_intro + str(text)
        # exhib_intro = re.sub(r'\s','',cate)
        print(exhib_intro)
        item['exhibIntro'] = exhib_intro
        yield item
        self.num += 1

    def parse(self, response):
        # pass
        div_list = response.xpath('/html/body/div[4]/div[3]/div/div[3]/div[@class="cszl-fent-s"]')
        for div in div_list:
            item = exhibitionItem()
            name = div.xpath('./h4/span/text()').extract_first()
            print(name)
            item['exhibName'] = name
            img = div.xpath('./a/img/@src').extract_first()
            print(img)
            item['exhibImg'] = img
            url = div.xpath('./a/@href').extract_first()
            # print(url)
            url = re.search(r'[a-z]+',url).group()
            # print(url)
            detail_url = 'https://cstm.cdstm.cn/cszl/' + url
            if detail_url != None:
                yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})