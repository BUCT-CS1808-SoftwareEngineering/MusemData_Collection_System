import scrapy
from museum.items import MuseumItem
# scrapy crawl museum1
# 故宫

class Museum1Spider(scrapy.Spider):
    name = 'museum1'
    # allowed_domains = ['www.xxx.com']
    start_urls = [
        'https://www.dpm.org.cn/Visit.html#block6'
        ]
    # start_urls = ['https://www.dpm.org.cn/Visit.html#block6']
    # for url in start_urls:
    #     yield scrapy.Request(url=url, callback=self.parse)
    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield Request(url = url,callback=self.parse)
    # def start_requests(self):
    #     # item = MuseumItem()
    #     url = {}
    #     url['url0'] = 'https://www.dpm.org.cn/Visit.html#block6' 
    #     # url['url1'] = 'https://www.dpm.org.cn/Visit.html#block6'
    #     url['url1'] = 'https://www.dpm.org.cn/Home.html'
    #     i = 0
    #     for i in range(2):
    #         con = 'url'+str(i)
    #         # con = format('url'%s)
    #         url_use = url[con]
    #         if i == 0:
    #             yield scrapy.Request(url=url_use, callback=self.parse_fir, meta={'item':item})
    #         if i == 1:
    #             yield scrapy.Request(url=url_use, callback=self.parse_thir, meta={'item':item})
    #         # if i == 2:
    #         #     yield scrapy.Request(url=url_use, callback=self.parse_thir)
    #     # yield item
            

        

    def parse(self, response):
        item = MuseumItem()
        # item=response.meta["item"]
        item['museumID'] = 1
        item['museumName'] = "故宫博物馆"
        # print(self.start_urls)
        item['museumLink'] = "https://www.dpm.org.cn/Home.html"
        # if self.url == 'https://www.dpm.org.cn/Visit.html#block6':
        time_hot = response.xpath('//*[@id="block3"]/div[2]/div[1]/h1/span[2]/text()').extract_first()
        time_open_hot = response.xpath('//*[@id="block3"]/div[2]/div[1]/ul/li[1]/span/text()').extract_first()
        time_pause_hot = response.xpath('//*[@id="block3"]/div[2]/div[1]/ul/li[2]/span/text()').extract_first()
        time_stop_hot = response.xpath('//*[@id="block3"]/div[2]/div[1]/ul/li[3]/span/text()').extract_first()
        time_close_hot = response.xpath('//*[@id="block3"]/div[2]/div[1]/ul/li[4]/span/text()').extract_first()
        time_off = response.xpath('//*[@id="block3"]/div[2]/div[2]/h1/span[1]/text()').extract_first()
        time_open_off = response.xpath('//*[@id="block3"]/div[2]/div[2]/ul/li[1]/span/text()').extract_first()
        time_pause_off = response.xpath('//*[@id="block3"]/div[2]/div[2]/ul/li[2]/span/text()').extract_first()
        time_stop_off = response.xpath('//*[@id="block3"]/div[2]/div[2]/ul/li[3]/span/text()').extract_first()
        time_close_off = response.xpath('//*[@id="block3"]/div[2]/div[2]/ul/li[4]/span/text()').extract_first()
        time1 = '旺季：' +  str(time_hot) + ' ' + str(time_open_hot) + ' ' + str(time_pause_hot) + ' ' + str(time_stop_hot) + ' ' + str(time_close_hot)
        time2 = '淡季：' +  str(time_off) + ' ' + str(time_open_off) + ' ' + str(time_pause_off) + ' ' + str(time_stop_off) + ' ' + str(time_close_off)
        time = time1 + ' ' + time2
        item['time'] = time
        print(item['time'])
        data = []
        cont = ''
        data_list = response.xpath('//*[@id="block6"]/div[1]/div/ul/li') 
        for li in data_list:
            m = li.xpath('./b/text()').extract_first()
            # print(m)
            data.append(m)
            # //*[@id="block6"]/div[1]/div/ul/li[2]/p/text()[1]
            m = li.xpath('./p/text()[1]').extract_first()
            # print(m)
            # //*[@id="block6"]/div[1]/div/ul/li[1]/p/text()[2]
            # //*[@id="block6"]/div[1]/div/ul/li[1]/p/text()[2]
            data.append(m)
            m = li.xpath('./p/text()[2]').extract_first()
            m = m.strip() + '。'
            # print(m)
            data.append(m)
        for i in range(len(data)):
            cont = cont + data[i]
        # print(cont)
        item['introduction'] = cont
        print(item['introduction'])
        url_use = 'https://www.dpm.org.cn/Home.html'
        yield scrapy.Request(url=url_use, callback=self.parse_thir, meta={'item':item})
        # yield item 
        # if url == 'https://www.dpm.org.cn/about/about_view.html':
        # data1 = response.xpath('/html/body/div[4]/div[2]/div/div[1]/p/text()').extract()
        # print(data1)
    
    # def parse_sec(self, response):
    #     # item = MuseumItem()
    #     data1 = response.xpath('/html/body/div[4]/div[2]/div/div[1]/p/text()').extract()
    #     print(data1)

    def parse_thir(self, response):
        # item = MuseumItem()
        item=response.meta["item"]
        comm = response.xpath('//*[@id="footer"]/div[1]/div[4]/div[1]/a/text()').extract_first()
        item['communication'] = comm
        print(item['communication'])
        yield item




