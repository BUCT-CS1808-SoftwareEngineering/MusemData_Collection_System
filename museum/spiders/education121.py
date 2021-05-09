import scrapy
from museum.items import educationItem
#
#scrapy crawl collection
#scrapy crawl exhiition
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
#scrapy genspider education
class Education9Spider(scrapy.Spider):
    name = 'education121'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.zgtcbwg.com/index.php?s=/Home/Article/lists/category/eduactvie.html']

    def parse(self, response):
        item = educationItem()
        #scrapy crawl education121
        _list = response.xpath('/html/body/div[1]/div[1]/div[2]/div[2]/section/div[1]/div')
        for li in _list:
            name = li.xpath('./a/text()').extract_first()
            name=name[1:len(name)]
            print(name)
            detail_url = li.xpath('./a/@href').extract_first()
            detail_url = 'http://www.zgtcbwg.com' + detail_url
            print(detail_url)
            yield scrapy.Request(url=detail_url,callback=self.parse_detail)
    def parse_detail(self, response):
        img = response.xpath('//*[@class="conbox"]//img/@src').extract_first()
        if img[0]!='h':
            img='http://www.zgtcbwg.com'+img
        #img = 'http://www.chnmus.net' + img
        print(img)
        cont=response.xpath('//*[@class="conbox"]//span//text()').extract()
        cont = ''.join(cont)
        print(cont)
