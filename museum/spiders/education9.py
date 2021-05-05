import scrapy
from museum.items import educationItem
# scrapy crawl education9
class Education9Spider(scrapy.Spider):
    name = 'education9'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.chnmus.net/sitesources/hnsbwy/page_pc/ppjy/sjyjjpxjd/pxdt/list1.html']

    def parse(self, response):
        item = educationItem()
        li_list = response.xpath('//*[@id="articleListTable"]/ul/li')
        # xp = '/html/body/div[1]/div/div[3]/div/div'
        # num = 1
        for li in li_list:
            name = li.xpath('./h5/a/text()').extract()
            name = ''.join(name)
            print(name)
            # item['exhibName'] = name
           
            # item['exhibImg'] = img
            detail_url = li.xpath('./h5/a/@href').extract_first()
            detail_url = 'http://www.chnmus.net' + detail_url
            print(detail_url)
            # self.deep_urls.append(detail_url)
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
        img = response.xpath('//*[@id="doZoom"]/p[2]/img/@src').extract()
        img = ''.join(img)
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
