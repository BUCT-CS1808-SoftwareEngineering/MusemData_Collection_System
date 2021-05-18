import scrapy
from selenium import webdriver
from njmusePro.items import collectionItem


class TjzrSpider(scrapy.Spider):
    name = 'collection189'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.tjnhm.com/index.php?p=jyhd_show&id=2107&lanmu=&c_id=16']

    model_urls = start_urls

    def __init__(self):
        self.bro = webdriver.Chrome(executable_path = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chromedriver.exe')

    def parse(self, response):
        try:
            title = response.xpath('//*[@id="aboutus_text"]/h1/text()').extract_first()
            img = 'https://www.tjnhm.com/' + response.xpath('//*[@id="aboutus_text"]/p[1]/span/img/@src').extract_first()
            p_list = response.xpath('//*[@id="aboutus_text"]//text()').extract()
            content = ''.join(p_list).replace('\r', '').replace('\n', ' ').split('上一条')[0]
            # content = ''
            # for i in p_list:
            #     content = content + i.xpath('./text()').extract_first()

            print(title, img, content)

            # url = 'https://www.tjnhm.com/' + response.xpath('//*[@id="aboutus_text"]/div[1]/a[3]/@href | //*[@id="aboutus_text"]/div[1]/a[4]/@href').extract_first()
            url = 'https://www.tjnhm.com/' + response.xpath('//*[@id="aboutus_text"]/div[1]/a[4]/@href').extract_first()
            if url:
                yield scrapy.Request(url, callback=self.parse)
        except:
            url = 'https://www.tjnhm.com/' + response.xpath('//*[@id="aboutus_text"]/div[1]/a[4]/@href').extract_first()
            if url:
                yield scrapy.Request(url, callback=self.parse)

    def closed(self,spider):
        self.bro.quit()
