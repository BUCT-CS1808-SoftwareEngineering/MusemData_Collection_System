import scrapy
from museum.items import educationItem
import re
# scrapy crawl education1
class Education1Spider(scrapy.Spider):
    name = 'education1'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.dpm.org.cn/Events.html']
    num = 0

    def parse_detail(self, response):
        item = response.meta["item"]
        name = response.xpath('/html/body/div[5]/div[2]/div/div[1]/div[1]/text()').extract()
        name = ''.join(name)
        print(name)
        item['eduName'] = name
        # time = response.xpath('/html/body/div[5]/div[2]/div/div[2]/div[2]/text()[1]/text()').extract_first()
        # print(time)
        #<p><strong>讲座提纲：</strong></p>\s([\s\S]*?)\s<p>
        content = response.xpath('/html/body/div[5]/div[2]/div/div[2]/div[2]').extract()
        content = ''.join(content)
        content = str(content)
        content = re.sub(r'<\/?.+?\/?>','',content)
        # content = ''.join(content)
        print(content)
        item['eduContent'] = content
        self.num += 1
        yield item

    def parse(self, response):
        
        # name = response.xpath('/html/body/div[4]/div[3]/div/div[2]')
        # print(name)
        div_list = response.xpath('/html/body/div[4]/div[3]/div/div[2]/div')
        # print(div_list)
        # //*[@id="hd1-4"]/div[2]/div/div[1]/div/div[4]/div[2]/a/h2
        for div in div_list:
            item = educationItem()
            item['museumID'] = 1
            img = div.xpath('./div[1]/a/img/@src').extract_first()
            print(img)
            item['eduImg'] = img
            # name = div.xpath('./div[2]/a/h2/text()').extract_first()
            # print(name)
            url_use = "https://www.dpm.org.cn/" + str(div.xpath('./div[1]/a/@href').extract_first())
            print(url_use)
            yield scrapy.Request(url_use,callback=self.parse_detail,meta={'item':item})
