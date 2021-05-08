import scrapy
from museum.items import educationItem
import re
# scrapy crawl education10

class Education11Spider(scrapy.Spider):
    name = 'education11'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.19371213.com.cn/learn/community/']

    def parse_detail(self, response):
        # if()
        item = response.meta["item"]
        # name = response.xpath('/html/body/div[5]/div[2]/div/div[1]/div[1]/text()').extract()
        # name = ''.join(name)
        # print(name)
        content = ''
        #node-6006 > section > div.submitted.hidden-xs.hidden-sm > div > div.date > span
        #node-3388 > section > div.submitted.hidden-xs.hidden-sm > div > div.date > span
        time = response.xpath('//section[@class="content-with-social-wrapper"]/div[3]/div/div[2]/span[1]/text()').extract_first()
        time = re.sub(r'\s','',time)
        # print(time)
        #<p><strong>讲座提纲：</strong></p>\s([\s\S]*?)\s<p>
        if response.xpath('//*[@id="node-3388"]/section/div[2]/div/div/div/div//text()').extract():
            content = response.xpath('//*[@id="node-3388"]/section/div[2]/div/div/div/div//text()').extract()
            # content = response.css('node-3388 > section > div.content-with-social-content > div > div > div *::text').extract()
            #node-3388 > section > div.content-with-social-content > div > div > div::text
            # //*[@id="node-3388"]/section/div[2]/div/div/div
            # //*[@id="node-3388"]/section/div[2]/div/div/div/style
            # //*[@id="node-3388"]/section/div[2]/div/div/div/div
            content = ''.join(content)
        # content = str(content)
            content = re.sub(r'\s','',content)
        content = content + "\n时间：" + time
        print(content)

    def parse(self, response):
        item = educationItem()
        # name = response.xpath('/html/body/div[4]/div[3]/div/div[2]')
        # print(name)
        div_list = response.xpath('//*[@id="views-bootstrap-grid-1"]/div/div')
        #views-bootstrap-grid-1 > div > div:nth-child(1)
        # /html/body/div[6]/div/div/div/div/div[2]/div/div/div[1]/div/div/div[2]
        # div_list = response.xpath('//*[@id="views-bootstrap-grid-1"]/div/div[1]/section/div[1]/div[1]/a/img')
        # print(div_list)
        # print(div_list)
        # //*[@id="hd1-4"]/div[2]/div/div[1]/div/div[4]/div[2]/a/h2
        for div in div_list:
            # //*[@id="views-bootstrap-grid-1"]/div/div[1]
            if div.xpath('./section/div[2]/header/h3/a/text()'):
                name = div.xpath('./section/div[2]/header/h3/a/text()').extract_first()
                print(name)
                img_new = div.xpath('./section/div[1]/div[1]/a/img/@src').extract_first()
                img_new = img_new.replace(".",'',1)
                img = "http://www.19371213.com.cn/learn/community" + img_new
                # //*[@id="views-bootstrap-grid-1"]/div/div[1]/section/div[2]/div
                # cont = div.xpath('./section/div[2]/div//text()').extract()
                # cont = 
                # # //*[@id="views-bootstrap-grid-1"]/div/div[1]/section/div[2]/div
                # cont = ''.join(cont)
                # # //*[@id="views-bootstrap-grid-1"]/div/div[1]/section/div[2]/div
                # time = div.xpath('./section/div[1]/div[2]/span[2]/text()').extract_first() + div.xpath('./section/div[1]/div[2]/span[1]/text()').extract_first()
                # time = re.sub(r'\s','',time)
                # cont = cont + "\n时间：" + time
                # print(cont)
                url_new = div.xpath('./section/div[1]/div[1]/a/@href').extract_first()
                url_new = url_new.replace(".",'',1)
                detail_url = "http://www.19371213.com.cn/learn/community" + url_new
                yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
