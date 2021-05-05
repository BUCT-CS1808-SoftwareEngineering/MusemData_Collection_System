import scrapy
from museum.items import exhibitionItem 
# scrapy crawl exhibition7

class Exhibition7Spider(scrapy.Spider):
    name = 'exhibition7'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.sxhm.com/index.php?page=1&ac=article&at=list&tid=196']

    def parse(self, response):
        item = exhibitionItem()
        div_list = response.xpath('/html/body/div[3]/div[2]/div[2]/ul/li')
        # xp = '/html/body/div[1]/div/div[3]/div/div'
        # num = 1
        for div in div_list:
            name = div.xpath('./a/span/text()').extract()
            name = ''.join(name)
            print(name)
            item['exhibName'] = name
            # img = div.xpath('./a/div[1]/img/@data-src').extract()
            # img = ''.join(img)
            # if img[0] == '/':
            #     img = 'http://www.njmuseum.com' + img
            # print(img)
            # item['exhibImg'] = img
            detail_url = div.xpath('./a/@href').extract_first()
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
        # if img[0] == '/':
        img = 'http://www.sxhm.com' + img
        print(img)
        # item['exhibImg'] = img
        cont = response.xpath('/html/body/div[3]/div[2]/div[2]/div[3]//text()').extract()
        cont = ''.join(cont)
        # time = response.xpath('//*[@id="展品概述"]/div[1]/div/div[2]/p[1]/span/text()').extract()
        # time = ''.join(time)
        # loca = response.xpath('//*[@id="展品概述"]/div[1]/div/div[2]/p[2]/span/text()').extract()
        # loca = ''.join(loca)
        # cont = cont + '\n展览时间：' + time + '\n展览地点：' + loca
        print(cont)
