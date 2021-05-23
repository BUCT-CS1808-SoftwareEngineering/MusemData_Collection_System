import scrapy
from museum.items import exhibitionItem 
# scrapy crawl exhibition9
class Exhibition9Spider(scrapy.Spider):
    name = 'exhibition9'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.chnmus.net/sitesources/hnsbwy/page_pc/clzl/jbcl/list1.html']
    new_urls = []
    deep_urls = []
    js1_urls = []
    js2_urls = []
    js3_urls = []
    num = 1

    def parse_detail(self, response):
        item = response.meta["item"]
        # exhib_name = div.xpath('./div[2]/div/div[1]/a[1]/text()').extract_first()
        
        cont = response.xpath('//*[@id="doZoom"]//text()').extract()
        cont = ''.join(cont)
        print(cont)
        item['exhibIntro'] = cont
        yield item
        self.num += 1
        # img = 
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
        # m = response.xpath('//*[@id="temporary2_list"]').extract()
        # print(m)
        # //*[@id="temporary2_list"]/div[1]
        # div_list = response.xpath('//*[@id="temporary2_list"]/div[1]/div')
        div_list = response.xpath('//*[@id="articleListTable"]/ul/li')
        for div in div_list:
            item = exhibitionItem()
            # //*[@id="temporary2_list"]/div[1]/div[1]/div[2]/div/div[1]/a[1]
            exhib_name = div.xpath('./a/h5/text()').extract_first()
            print(exhib_name)
            detail_url = 'http://www.chnmus.net' + div.xpath('./a/@href').extract_first()
            img = 'http://www.chnmus.net' + div.xpath('./a/img/@src').extract_first()
            # print(exhib_name)
            print(img)
            item['exhibName'] = exhib_name
            item['museumID'] = 9
            item['exhibImg'] = img
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
