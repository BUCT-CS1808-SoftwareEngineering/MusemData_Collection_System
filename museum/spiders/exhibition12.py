import scrapy
from  selenium import webdriver 
from museum.items import exhibitionItem 
# scrapy crawl exhibition12
class Exhibition12Spider(scrapy.Spider):
    name = 'exhibition12'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xxx.com/']

    start_urls = ['http://www.ssmzd.com/jngclzl/LinShiZhanLan/Index.html']
    new_urls = ['http://www.ssmzd.com/jngclzl/LinShiZhanLan/Index.html']
    # deep_urls = []
    num = 1


    #实例化一个
    def __init__(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        self.bro = webdriver.Firefox(options=options)
        # self.brom = webdriver.Firefox()
    def parse(self, response):
        div_list = response.xpath('/html/body/table[2]/tbody/tr/td/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table')
        # xp = '/html/body/div[1]/div/div[3]/div/div'
        # num = 1
        for div in div_list:
            if div.xpath('./tbody/tr/td[2]/table[1]/tbody/tr/td/a/text()').extract():
                item = exhibitionItem()
                name = div.xpath('./tbody/tr/td[2]/table[1]/tbody/tr/td/a/text()').extract()
                # /html/body/table[2]/tbody/tr/td/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td/a
                # /html/body/table[2]/tbody/tr/td/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table
                # /html/body/table[2]/tbody/tr/td/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table[2]/tbody/tr/td[2]/table[2]/tbody/tr/td
                # /html/body/table[2]/tbody/tr/td/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table[2]/tbody/tr/td[1]/table/tbody/tr/td/a/img
                name = ''.join(name)
                print(name)
                item['exhibName'] = name
                img = div.xpath('./tbody/tr/td[1]/table/tbody/tr/td/a/img/@src').extract()
                img = ''.join(img)
                # if img[0] == '/':
                img = 'http://www.ssmzd.com' + img
                print(img)
                item['exhibImg'] = img
                # detail_url = "http://www.njmuseum.com" + div.xpath('./a/@href').extract_first()
                # print(detail_url)
                cont = div.xpath('.//tbody/tr/td[2]/table[2]/tbody/tr/td//text()').extract()
                cont = ''.join(cont)
                print(cont)
                item['exhibIntro'] = cont
                item['museumID'] = 12
                yield item
                self.num += 1
            # self.deep_urls.append(detail_url)
            # yield scrapy.Request(url=detail_url,callback=self.parse_detail)
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
    
    # def parse_detail(self, response):
    #     cont = response.xpath('//*[@id="展品概述"]/div[1]/div/div[1]//text()').extract()
    #     cont = ''.join(cont)
    #     time = response.xpath('//*[@id="展品概述"]/div[1]/div/div[2]/p[1]/span/text()').extract()
    #     time = ''.join(time)
    #     loca = response.xpath('//*[@id="展品概述"]/div[1]/div/div[2]/p[2]/span/text()').extract()
    #     loca = ''.join(loca)
    #     cont = cont + '\n展览时间：' + time + '\n展览地点：' + loca
    #     print(cont)

    def closed(self,spider):
        self.bro.quit()
        # self.brom.quit()
