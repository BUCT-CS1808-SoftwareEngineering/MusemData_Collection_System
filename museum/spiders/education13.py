import scrapy
from selenium import webdriver
from museum.items import educationItem
# scrapy crawl education13

class Education13Spider(scrapy.Spider):
    name = 'education13'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.wuhouci.net.cn/xshd.html']

    new_urls = ['http://www.wuhouci.net.cn/xshd.html']
    # deep_urls = []

    # def start_requests(self):
    #     url = 'http://www.njmuseum.com/zh/educationIndex'
    #     # FormRequest 是Scrapy发送POST请求的方法，但是没有解决问题
    #     # yield scrapy.FormRequest(
    #     #     headers={'Content-Type': 'application/json'},
    #     #     method = 'POST',
    #     #     url = IP_PORT,
    #     #     formdata = json.dumps(self.data)
    #     #     callback = self.parse
    #     #     # dont_filter = True
    #     # )
 
    #     # 最后不得不采用request直接解决了。。
        # yield scrapy.Request(url = IP_PORT, method='POST',callback = self.parse)

    #实例化一个
    def __init__(self):
        self.bro = webdriver.Firefox()
        # self.brom = webdriver.Firefox()
    def parse(self, response):
        item = educationItem()
        # /html/body/section[2]/div[2]/div[2]/ul
        li_list = response.xpath('/html/body/section[2]/div[2]/div[2]/ul/li')
        # print(li_list)
        # xp = '/html/body/div[1]/div/div[3]/div/div'
        # num = 1
        for li in li_list:
            name = li.xpath('./div[@class="title"]//text()').extract()
            name = ''.join(name)
            print(name)
            img = li.xpath('./div[@class="l"]/img[1]/@src').extract()
            img = ''.join(img)
            img = 'http://www.wuhouci.net.cn' + img
            print(img)
            cont = li.xpath('./div[@class="r"]/div[2]//text()').extract()
            cont = ''.join(cont)
            time = li.xpath('./div[2]/div[3]/div[2]//text()').extract()
            # /html/body/section[2]/div[2]/div[2]/ul/li[1]/div[2]/div[3]/div[2]
            time = ''.join(time)
            cont = cont + '\n时间：' + time
            print(cont)
            # item['exhibName'] = name
           
            # item['exhibImg'] = img
            # detail_url = li.xpath('./form/@action').extract_first()
            # print(detail_url)
            # self.deep_urls.append(detail_url)
            # yield scrapy.Request(url=detail_url,callback=self.parse_detail,method='POST')
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
    #     img = li.xpath('/html/body/div[3]/div[2]/div/ul[2]/li[1]/p/img/@src').extract()
    #     img = ''.join(img)
    #     img = 'https://activity.wisdommuseum.cn' + img
    #     print(img)
    #     cont = response.xpath('/html/body/div[3]/div[2]/div/ul[3]/li[1]/pre//text()').extract()
    #     cont = ''.join(cont)
    #     time = response.xpath('/html/body/div[3]/div[2]/div/ul[2]/li[2]/span[2]/text()').extract()
    #     time = ''.join(time)
    #     loca = response.xpath('/html/body/div[3]/div[2]/div/ul[2]/li[2]/span[4]/text()').extract()
    #     loca = ''.join(loca)
    #     # time = response.xpath('//*[@id="app"]/div/div/div/div/main/div[1]/div[3]/div[2]/div[1]/div[1]/p/text()').extract()
    #     # time = ''.join(time)
    #     # loca = response.xpath('//*[@id="app"]/div/div/div/div/main/div[1]/div[3]/div[2]/div[1]/div[2]/p/text()').extract()
    #     # loca = ''.join(loca)
    #     cont = cont + '\n展览时间：' + time + '\n展览地点：' + loca
    #     print(cont)

    def closed(self,spider):
        self.bro.quit()
        # self.brom.quit()
