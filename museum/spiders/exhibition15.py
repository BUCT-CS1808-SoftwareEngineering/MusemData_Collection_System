import scrapy
from museum.items import exhibitionItem 
import re
# scrapy crawl exhibition15
class Exhibition15Spider(scrapy.Spider):
    name = 'exhibition15'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.njmuseumadmin.com/Exhibition/review/id/22']

    def parse_detail(self, response):
        item = response.meta["item"]
        cont = response.xpath('//*[@id="form"]/div[3]/div[2]/div/div[2]/dl//text()').extract()
        cont = ''.join(cont)
        des = response.xpath('//*[@id="form"]/div[3]/div[3]//text()').extract()
        des = ''.join(des)
        cont = cont + des
        cont = re.sub('&(.+?);','',cont)
        name = response.xpath('//*[@id="form"]/div[3]/div[2]/div/div[2]/span/text()').extract_first()
        print(name)
        print(cont)
        # exhib_time = response.xpath('/html/body/div/div[3]/div[1]/div/div[3]/div/p[1]/span[1]/em/text()').extract_first()
        # exhib_location = response.xpath('/html/body/div/div[3]/div[1]/div/div[3]/div/p[1]/span[2]/em/text()').extract_first()
        # exhib_intro = response.xpath('/html/body/div/div[3]/div[1]/div/div[3]/div/p[3]/text()').extract()
        # s = ''
        # for i in range(len(exhib_intro)):
        #     exhib_intro[i] = str(exhib_intro[i])
        #     s += re.sub(r'\\u3000','',exhib_intro[i])     
        # print(exhib_time)
        # print(exhib_location)
        # print(s)
        # yield item

    # https://www.dpm.org.cn/searchs/exhibition/category_id/301/pagesize/6/tpl_file/shows_temporary2_2/exhibition_status/0/showstype/301/order/1/p/2.html

    def parse(self, response):
        item = exhibitionItem()
        # m = response.xpath('//*[@id="temporary2_list"]').extract()
        # print(m)
        # //*[@id="temporary2_list"]/div[1]
        # div_list = response.xpath('//*[@id="temporary2_list"]/div[1]/div')
        div_list = response.xpath('//*[@id="form"]/div[3]/div/div[3]/div[@class="review_listcon"]')
        for div in div_list:
            # //*[@id="temporary2_list"]/div[1]/div[1]/div[2]/div/div[1]/a[1]
            # exhib_name = div.xpath('./div[2]/div/div[1]/a[1]/text()').extract_first()
            # if exhib_name != None:
            #     print(exhib_name)
            img = div.xpath('./a/img/@src').extract_first()
            img = "http://www.njmuseumadmin.com" + img
            print(img)
            detail_url = div.xpath('./a/@href').extract_first()
            detail_url = "http://www.njmuseumadmin.com" + detail_url
            # if detail_url != None:
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
