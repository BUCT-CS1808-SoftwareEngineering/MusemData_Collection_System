import scrapy
from museum.items import educationItem
# scrapy crawl education10

class Education10Spider(scrapy.Spider):
    name = 'education10'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.hongyan.info/list/59']
    new_urls = []
    deep_urls = []
    js1_urls = []
    js2_urls = []
    js3_urls = []
    num = 1

    def parse(self, response):
        li_list = response.xpath('/html/body/div[8]/div[2]/div[1]/ul/li')
        # xp = '/html/body/div[1]/div/div[3]/div/div'
        # num = 1
        for li in li_list:
            item = educationItem()
            name = li.xpath('./a/text()').extract()
            name = ''.join(name)
            print(name)
            # item['exhibName'] = name
           
            # item['exhibImg'] = img
            detail_url = li.xpath('./a/@href').extract_first()
            detail_url = 'https://www.hongyan.info' + detail_url
            print(detail_url)
            item['eduName'] = name
            item['museumID'] = 10
            # self.deep_urls.append(detail_url)
            yield scrapy.Request(url=detail_url,callback=self.parse_detail,meta={'item':item})
            # print(detail_url)
            # brom = webdriver.Firefox()
            # brom.get(detail_url)
            # page_textl = brom.page_source
            # # 点击跳转
            # # xp = div.xpath('./div[1]/a')[0]
            # # xp_use = xp + '[' + str(num) + ']' + '/div[1]'
            # # num  += 1
            # # # print(xp)
            # # a_click = bro.find_element_by_xpath(xp_use)
            # # a_click.click() 
            # treel = etree.HTML(page_textl)
            # cont = treel.xpath('/html/body/div[1]/div/div[5]/p')[0].text
            # text = treel.xpath('/html/body/div[1]/div/div[4]/span[1]/text()')
            # text = ''.join(text)
            # cont = cont + ' '  + text 
            # item['exhibIntro'] = cont
            # print(cont)
            # brom.quit()
            # yield item


        # sleep(5)
        # bro.quit()
    
    def parse_detail(self, response):
        item = response.meta["item"]
        # body > div.main > div.main-right.fr > div.main-content > div.content-all > p:nth-child(3) > img
        # body > div.main > div.main-right.fr > div.main-content > div.content-all > p:nth-child(3) > img
        # body > div.main > div.main-right.fr > div.main-content > div.content-all > p:nth-child(2) > img
        # img = response.css('div.content-all img::attr(src)').extract_first()
        # # img = ''.join(img)
        # if img:
        #     img = 'https://www.hongyan.info' + img
        img = response.xpath('/html/body/div[8]/div[2]/div[3]/div[2]//img/@src').extract_first()
        if img[0] == '/':
            img = 'https://www.hongyan.info' + img
        print(img)
        cont = response.xpath('//div[@class="content-all"]//text()').extract()
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
