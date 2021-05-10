import scrapy
from museum.items import educationItem
# scrapy crawl education22

class Education22Spider(scrapy.Spider):
    name = 'education22'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.artmuseum.tsinghua.edu.cn/ggjy/ztjz/jzyy/']

    def parse(self, response):
        item = educationItem()
        num = 1
        li_list = response.xpath('/html/body/div[4]/div[3]/div/div/div[2]/ul/li')
        for li in li_list:
            if num > 6:
                break
            num += 1
            name = li.xpath('./a/text()').extract()
            name = ''.join(name)
            print(name)
            detail_url = li.xpath('./a/@href').extract_first()
            cont = "详情参见：" + detail_url
            print(cont)
            yield scrapy.Request(url=detail_url,callback=self.parse_detail)
    
    def parse_detail(self, response):
        img = response.xpath('//*[@id="page-content"]//img/@data-src').extract_first()
        print(img)
        # cont = response.xpath('//*[@id="js_content"]/section[2]/section/section//text()').extract()
        # cont = ''.join(cont)
