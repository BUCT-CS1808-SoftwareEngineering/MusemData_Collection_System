import scrapy
from  selenium import webdriver 
from museum.items import exhibitionItem 
# scrapy crawl exhibition5
class Exhibition5Spider(scrapy.Spider):
    name = 'exhibition5'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.zhejiangmuseum.com/Exhibition/TemporaryExhibition']
    new_urls = ['http://www.zhejiangmuseum.com/Exhibition/TemporaryExhibition']
    deep_urls = []


    #实例化一个
    def __init__(self):
        self.bro = webdriver.Firefox()
        self.brom = webdriver.Firefox()
    def parse(self, response):
        item = exhibitionItem()
        li_list = response.xpath('//*[@id="app"]/div/div/div/div/main/ul[2]/li')
        # xp = '/html/body/div[1]/div/div[3]/div/div'
        # num = 1
        for li in li_list:
            name = li.xpath('./div[1]/a/h3/text()').extract()
            name = ''.join(name)
            print(name)
            item['exhibName'] = name
            img = li.xpath('./figure/img/@src').extract()
            img = ''.join(img)
            print(img)
            item['exhibImg'] = img
            detail_url = "http://www.zhejiangmuseum.com" + li.xpath('./div[1]/a/@href').extract_first()
            print(detail_url)
            self.deep_urls.append(detail_url)
            yield scrapy.Request(url=detail_url,callback=self.parse_detail)
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
        cont = response.xpath('//*[@id="app"]/div/div/div/div/main/div[1]/div[4]//text()').extract()
        cont = ''.join(cont)
        time = response.xpath('//*[@id="app"]/div/div/div/div/main/div[1]/div[3]/div[2]/div[1]/div[1]/p/text()').extract()
        time = ''.join(time)
        loca = response.xpath('//*[@id="app"]/div/div/div/div/main/div[1]/div[3]/div[2]/div[1]/div[2]/p/text()').extract()
        loca = ''.join(loca)
        cont = cont + '\n展览时间：' + time + '\n展览地点：' + loca
        print(cont)

    def closed(self,spider):
        self.bro.quit()
        self.brom.quit()
