import scrapy
from scrapy import item
from  selenium import webdriver 
from museum.items import exhibitionItem 
# scrapy crawl exhibition6

class Exhibition6Spider(scrapy.Spider):
    name = 'exhibition6'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.njmuseum.com/zh/exhibitionIndex']
    new_urls = ['http://www.njmuseum.com/zh/exhibitionIndex']
    deep_urls = []
    num = 1


    #实例化一个
    def __init__(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        self.bro = webdriver.Firefox(options=options)
        self.brom = webdriver.Firefox(options=options)
    def parse(self, response):
        div_list = response.xpath('//*[@id="exhibitionIndex"]/div[2]/div[4]/div')
        # xp = '/html/body/div[1]/div/div[3]/div/div'
        # num = 1
        for div in div_list:
            item = exhibitionItem()
            name = div.xpath('./a/div[2]/h5/text()').extract()
            name = ''.join(name)
            print(name)
            item['exhibName'] = name
            img = div.xpath('./a/div[1]/img/@data-src').extract()
            img = ''.join(img)
            if img[0] == '/':
                img = 'http://www.njmuseum.com' + img
            print(img)
            item['exhibImg'] = img
            detail_url = "http://www.njmuseum.com" + div.xpath('./a/@href').extract_first()
            print(detail_url)
            self.deep_urls.append(detail_url)
            item['exhibName'] = name
            item['exhibImg'] = img
            item['museumID'] = 6
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
        cont = response.xpath('//*[@id="展品概述"]/div[1]/div/div[1]//text()').extract()
        cont = ''.join(cont)
        time = response.xpath('//*[@id="展品概述"]/div[1]/div/div[2]/p[1]/span/text()').extract()
        time = ''.join(time)
        loca = response.xpath('//*[@id="展品概述"]/div[1]/div/div[2]/p[2]/span/text()').extract()
        loca = ''.join(loca)
        cont = cont + '\n展览时间：' + time + '\n展览地点：' + loca
        print(cont)
        item['exhibIntro'] = cont
        yield item
        self.num += 1

    def closed(self,spider):
        self.bro.quit()
        self.brom.quit()
