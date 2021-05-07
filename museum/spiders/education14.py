import scrapy
from selenium import webdriver
from museum.items import educationItem
# scrapy crawl education14
class Education14Spider(scrapy.Spider):
    name = 'education14'
    # allowed_domains = ['www.xxx.com']
    # start_urls = ['http://39.98.66.177/QinLing/PhotoGallery']
    start_urls = ['http://www.bmy.com.cn/html/public/jy/c5c2ef446a8e46e9848b8e264e0f187b.html']

    new_urls = ['http://www.bmy.com.cn/html/public/jy/c5c2ef446a8e46e9848b8e264e0f187b.html']
    deep_urls = []

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
        self.brom = webdriver.Firefox()
    def parse(self, response):
        item = educationItem()
        li_list = response.xpath('/html/body/div[2]/div[1]/div[1]/div')
        # xp = '/html/body/div[1]/div/div[3]/div/div'
        # num = 1
        for li in li_list:
            name = li.xpath('./p[2]/text()').extract()
            name = ''.join(name)
            print(name)
            # item['exhibName'] = name
           
            # item['exhibImg'] = img
            detail_url = li.xpath('./a/@href').extract_first()
            print(detail_url)
            self.deep_urls.append(detail_url)
            img = li.xpath('./a/img/@src').extract()
            img = ''.join(img)
            # img = 'https://activity.wisdommuseum.cn' + img
            print(img)
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
        cont = response.xpath('/html/body/div[2]/div[4]//text()').extract()
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

    def closed(self,spider):
        self.bro.quit()
        self.brom.quit()