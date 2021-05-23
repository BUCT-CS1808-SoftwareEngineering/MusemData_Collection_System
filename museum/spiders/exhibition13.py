import scrapy
from  selenium import webdriver 
from museum.items import exhibitionItem 
import re
# scrapy crawl exhibition13
class Exhibition13Spider(scrapy.Spider):
    name = 'exhibition13'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.wuhouci.net.cn/ztzl.html']

    new_urls = ['http://www.wuhouci.net.cn/ztzl.html']
    # deep_urls = []
    # url = "http://www.wuhouci.net.cn/ztzl-detail.html#id=%s"
    num = 1


    #实例化一个
    def __init__(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        self.bro = webdriver.Firefox(options=options)
        # self.brom = webdriver.Firefox()
    def parse(self, response):
        div_list = response.xpath('/html/body/section[2]/div[2]/div[3]/ul//li')
        # data_list = response.xpath('/html/body/section[2]/div[2]/div[3]/ul/li//@data-id').extract()
        # num = 0
        # xp = '/html/body/div[1]/div/div[3]/div/div'
        # num = 1
        for div in div_list:
            item = exhibitionItem()
            name = div.xpath('./div[2]/div[@class="title"]/text()').extract()
            name = ''.join(name)
            print(name)
            item['exhibName'] = name
            # if div.xpath('./div[2]/div[@class="des"]//text()'):
            cont = div.xpath('./div[2]/div[@class="des"]//text()').extract()
            cont = ''.join(cont)
            time = div.xpath('./div[2]/div[@class="date a"]/div[@class="d2"]//text()').extract()
            time = ''.join(time)
            cont = cont + "\n展览时间：" + time
            print(cont)
            img = div.xpath('./div[1]/div[1]/@style').extract_first()
            img = "http://www.wuhouci.net.cn" + re.search('(?<=\()\S+(?=\))',img).group()
            print(img)
            item['exhibImg'] = img
            item['exhibName'] = name
            item['exhibIntro'] = cont
            item['museumID'] = 13
            yield item
            self.num += 1
            # item['exhibImg'] = img
            # coid = div.xpath('./@data-id').extract()
            # coid = ''.join(coid)
            # detail_url = self.url%div.xpath('./@data-id').extract_first()
            # self.deep_urls.append(detail_url)
            # print(detail_url)
            # yield scrapy.Request(url=detail_url,callback=self.parse_detail)
            # num += 1
            # print(detail_url)

        # print(self.deep_urls)
        # for url in self.deep_urls:
        #     yield scrapy.Request(url=url,callback=self.parse_detail)
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
    #     # img = response.xpath('//*[@id="eq"]/div[2]/div[2]/div[1]/ul/li[1]/img/@src').extract()
    #     # img = ''.join(img)
    #     # # if img[0] == '/':
    #     # img = 'http://www.wuhouci.net.cn' + img
    #     # print(img)
    #     cont = response.xpath('//*[@id="eq"]/div[2]/div[3]//text()').extract()
    #     cont = ''.join(cont)
    #     time = response.xpath('//*[@id="eq"]/div[2]/div[2]/div[2]/ul/li[2]/summary/text()').extract()
    #     time = ''.join(time)
    #     loca = response.xpath('//*[@id="eq"]/div[2]/div[2]/div[2]/ul/li[4]/summary/text()').extract()
    #     loca = ''.join(loca)
    #     cont = cont + '\n展览时间：' + time + '\n展览地点：' + loca
    #     print(cont)

    def closed(self,spider):
        self.bro.quit()
        # self.brom.quit()
