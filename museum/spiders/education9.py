import scrapy
from museum.items import educationItem
# scrapy crawl education9
class Education9Spider(scrapy.Spider):
    name = 'education9'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.chnmus.net/sitesources/hnsbwy/page_pc/ppjy/sjyjjpxjd/pxdt/list1.html']
    new_urls = []
    deep_urls = []
    js1_urls = []
    js2_urls = []
    js3_urls = []
    num = 1

    def parse(self, response):
        li_list = response.xpath('//*[@id="articleListTable"]/ul/li')
        # xp = '/html/body/div[1]/div/div[3]/div/div'
        # num = 1
        for li in li_list:
            item = educationItem()
            name = li.xpath('./h5/a/text()').extract()
            name = ''.join(name)
            print(name)
            item['eduName'] = name
            item['museumID'] = 9
            # item['exhibImg'] = img
            detail_url = li.xpath('./h5/a/@href').extract_first()
            detail_url = 'http://www.chnmus.net' + detail_url
            print(detail_url)
            # self.deep_urls.append(detail_url)
            yield scrapy.Request(url=detail_url,callback=self.parse_detail,meta={'item':item})
            # yield item


        # sleep(5)
        # bro.quit()
    
    def parse_detail(self, response):
        item = response.meta["item"]
        img = response.xpath('//*[@id="doZoom"]//img/@src').extract_first()
        # img = ''.join(img)
        img = 'http://www.chnmus.net' + img
        print(img)
        cont = response.xpath('//*[@id="doZoom"]//text()').extract()
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
        item['eduContent'] = cont
        item['eduImg'] = img
        yield item
        self.num += 1
