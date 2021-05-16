import scrapy
from museum.items import exhibitionItem


class Exhibition60Spider(scrapy.Spider):
    name = 'exhibition60'
    start_urls = [
        "http://www.gzmuseum.com/zl/zlhg/"
    ]

    def parse(self, response):
        item = exhibitionItem()
        title_list = response.xpath(
            "//div[@class='zlhg_list']//h2/a/text()").getall()
        description_list = response.xpath(
            "//div[@class='zlhg_ms f_l']/p/text()").getall()
        img_list = response.xpath(
            "//div[@class='zlhg_list']//img/@src").getall()
        print(description_list)
        for index, i in enumerate(img_list):
            exhibitionName = "".join(title_list[index].split())
            if(index >= 3):
                exhibitionDescription = description_list[index-3]
            else:
                exhibitionDescription = "无介绍"
            exhibitionImageUrl = i
            print((exhibitionName, exhibitionImageUrl, exhibitionDescription))
