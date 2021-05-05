import scrapy
from  selenium import webdriver 
from museum.items import exhibitionItem 
# scrapy crawl exhibition8
class Exhibition8Spider(scrapy.Spider):
    name = 'exhibition8'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.shanghaimuseum.net/mu/frontend/pg/display/offline-exhibit']
    new_urls = ['https://www.shanghaimuseum.net/mu/frontend/pg/display/offline-exhibit']
    deep_urls = []
    js1_urls = []
    js2_urls = []

    def __init__(self):
        self.bro = webdriver.Firefox()
        self.brom = webdriver.Firefox()
    def parse(self, response):
        item = exhibitionItem()
        # item = collectionItem()
        # //*[@id="building2"]/div/div[2]/table/tbody
        li_list = response.xpath('//*[@id="list1"]/li')
        # print(coll_list)
        # for i in range(2):
        for div in li_list:
            # if li.xpath('./td/a/text()').extract_first() != None:
                # //*[@id="227613"]/text()
            name = div.xpath('./div[2]/text()').extract_first()
            # coll_name = ''.join(coll_name)
            print(name)
            # print(li.xpath('./td/a/@href').extract_first())
            detail_url = 'https://www.shanghaimuseum.net/mu/' + div.xpath('./div[1]/a/@href').extract_first()
            # img = div.xpath('./div[1]/div[1]/a/img/@src').extract_first()
            # # if img[0] == '/':
            # #     img = 'http://www.zhejiangmuseum.com' + img
            # img = 'https://www.shanghaimuseum.net/mu/' + img
            # print(img)
            self.deep_urls.append(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
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
        # coll_name = response.xpath('//*[@id="hl_content"]/div/div[2]/h3/span/text()').extract_first()
        # time = 'None'
        # if response.xpath('//*[@id="app"]/div/div/div/div/main/div/div[2]/div[2]/div[1]/div[1]/p/text()').extract():
        #     time = response.xpath('//*[@id="app"]/div/div/div/div/main/div/div[2]/div[2]/div[1]/div[1]/p/text()').extract_first()
        img = response.xpath('/html/body/div[4]/div/div/div[1]/img/@src').extract()
        img = ''.join(img)
            # if img[0] == '/':
            #     img = 'http://www.zhejiangmuseum.com' + img
        img = 'https://www.shanghaimuseum.net/mu/' + img
        print(img)
        coll_desc = response.xpath('/html/body/div[4]/div/div/div[2]//text()').extract()
        coll_desc = ''.join(coll_desc)
        print(coll_desc)

    def closed(self,spider):
        self.bro.quit()
        self.brom.quit()
