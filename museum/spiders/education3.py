import scrapy
from selenium import webdriver
from museum.items import educationItem
#scrapy crawl education4
class Education3Spider(scrapy.Spider):
    name = 'education3'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.sstm.org.cn/activeedu']
    new_urls = ['http://www.sstm.org.cn/activeedu']
    deep_urls = []


    #实例化一个
    def __init__(self):
        self.bro = webdriver.Firefox()
        # self.brom = webdriver.Firefox()
    def parse(self, response):
        item = educationItem()
        div_list = response.xpath('/html/body/div[1]/div/div[4]/div[2]/div[@class="item clearfix"]')
        # xp = '/html/body/div[1]/div/div[3]/div/div'
        # num = 1
        for div in div_list:
            name = div.xpath('./div[5]/div[1]/text()').extract()
            name = ''.join(name)
            print(name)
            # item['exhibName'] = name
            img = div.xpath('./div[4]/@data-src').extract()
            img = ''.join(img)
            print(img)
            # item['exhibImg'] = img
            time = div.xpath('./div[5]/div[2]/span[2]/text()').extract()
            time = ''.join(time)
            cont = div.xpath('./div[5]/div[3]/div[3]/text()').extract()
            cont = ''.join(cont)
            cont = cont + ' 活动时间：' + time
            print(cont)
            # detail_url = "http://www.sstm.org.cn" + str(div.xpath('./div[1]/a/@href').extract_first())
            # print(detail_url)
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
    #     cont = response.xpath('/html/body/div[1]/div/div[5]/p/text()').extract()
    #     cont = ''.join(cont)
    #     text = response.xpath('/html/body/div[1]/div/div[4]/span[1]/text()').extract()
    #     text = ''.join(text)
    #     cont = cont + text
    #     print(cont)

    def closed(self,spider):
        self.bro.quit()
        # self.brom.quit()
