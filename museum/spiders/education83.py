import scrapy

#动态加载
class Education83Spider(scrapy.Spider):
    name = 'education83'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.zhongshanwarship.org.cn/shejiao.html']

    def parse(self, response):
        pass
