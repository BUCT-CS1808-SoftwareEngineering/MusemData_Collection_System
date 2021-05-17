import scrapy
from museum.items import exhibitionItem
#爬取数据为空
class Exhibition98Spider(scrapy.Spider):
    name = 'exhibition98'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.lymuseum.com/bencandy.php?fid=60&id=37']

    def parse(self, response):
        item = exhibitionItem()
        
        #exhib_list = response.xpath('/html/body/div[4]/div')
        
        #for div in exhib_list:
            #/html/body/div[4]/div[1]/ul/li/a/p[1]
        exhib_name = response.xpath('/html/body/div[6]/div[4]/div[1]/div[9]/table/tbody/tr[1]/td/table[1]/tbody/tr[1]/td/b//text()').extract()
        exhib_name = ''.join(exhib_name)
        print(exhib_name)
            #/html/body/div[4]/div[1]/ul/img
            #exhib_img = div.xpath('./ul/img/@src').extract_first()
            
            #exhib_img = 'http://www.hnzzmuseum.com' + exhib_img
            #print(exhib_img)  
            #/html/body/div[4]/div[1]/ul/li/a/p[2]/span 
            #exhib_desc = div.xpath('./ul/li/a/p[2]/span//text()').extract()
            #exhib_desc = ''.join(exhib_desc)
            #print(exhib_desc)  
