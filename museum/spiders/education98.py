import scrapy
from museum.items import educationItem
#输出为空
class Education98Spider(scrapy.Spider):
    name = 'education98'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.lymuseum.com/list.php?fid=70']

    #def parse_detail(self, response):
        #item = response.meta["item"]
        #/html/body/div/div[1]/div[3]/div/div[2]/div[3]/div
        #if response.xpath('/html/body/div[4]/ul/li[3]/p//text()'):
            #edu_desc = response.xpath('/html/body/div[4]/ul/li[3]/p//text()').extract()
            #edu_desc = ''.join(edu_desc)
            #print(edu_desc)  

    def parse(self, response):
        item = educationItem()
        
        #edu_list = response.xpath('/html/body/div[4]/div')
        #//*[@id="thumbnailUL"]
        #for div in edu_list:
            #/html/body/div[4]/div[2]/div[1]/a/p[1] /html/body/div[6]/div[4]/div[1]/div[9]/div/table/tbody/tr[1]/td/table[2]/tbody/tr[1]/td[2]/a/b
        edu_name = response.xpath('/html/body/div[6]/div[4]/div[1]/div[9]/div/table/tbody/tr[1]/td/table[2]/tbody/tr[1]/td[2]/a/b/text()').extract_first()
        print(edu_name)
            #/html/body/div[4]/div[2]/div[1]/a
            #detail_url = div.xpath('./div[1]/a/@href').extract_first()
            #http://www.hnzzmuseum.com
            #http://www.hnzzmuseum.com
            #detail_url = 'http://www.pdsm.org.cn' + li.xpath('./div[2]/a/@href').extract_first()
            #detail_url = 'http://www.hnzzmuseum.com' + detail_url
            #yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})

