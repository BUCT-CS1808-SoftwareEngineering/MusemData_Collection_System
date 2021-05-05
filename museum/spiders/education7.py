import scrapy
from museum.items import educationItem
# scrapy crawl education7
class Education7Spider(scrapy.Spider):
    name = 'education7'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.sxhm.com/index.php?ac=article&at=list&tid=216']

    def parse(self, response):
        item = educationItem()
        li_list = response.xpath('/html/body/div[3]/div[2]/div[2]/ul/li')
        # xp = '/html/body/div[1]/div/div[3]/div/div'
        # num = 1
        for li in li_list:
            name = li.xpath('./a/text()').extract()
            name = ''.join(name)
            print(name)
            # item['exhibName'] = name
           
            # item['exhibImg'] = img
            detail_url = li.xpath('./a/@href').extract_first()
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
        img = response.xpath('/html/body/div[3]/div[2]/div[2]/div[3]/p[2]/img[1]/@src').extract()
        img = ''.join(img)
        img = 'http://www.sxhm.com' + img
        print(img)
        cont = response.xpath('/html/body/div[3]/div[2]/div[2]/div[3]//text()').extract()
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
