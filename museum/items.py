# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# 基本信息已在百科中爬取，可不爬
class MuseumItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    museumID = scrapy.Field()   
    museumName = scrapy.Field()  
    museumForName = scrapy.Field()
    introduction = scrapy.Field()
    time = scrapy.Field() 
    # opentime=scrapy.Field()
    # museumLink = scrapy.Field()
    location = scrapy.Field()
    # communication = scrapy.Field()
    category = scrapy.Field()
    price = scrapy.Field()
    # latiLong = scrapy.Field()

# 藏品信息
class collectionItem(scrapy.Item):
    museumID = scrapy.Field()  # 博物馆ID，表中自带字段，可不爬
    collectionID = scrapy.Field() # 藏品ID，可不爬
    collectionName = scrapy.Field() # 藏品名称
    collectionIntroduction = scrapy.Field() # 藏品简介
    collectionImage = scrapy.Field() # 藏品图片链接

class exhibitionItem(scrapy.Item):
    museumID = scrapy.Field() # 博物馆ID，表中自带字段，可不爬
    exhibID = scrapy.Field()  # 展览ID，可不爬
    exhibImg = scrapy.Field()  # 展览图片
    exhibName = scrapy.Field() # 展览名称
    # exhibTime = scrapy.Field()
    # exhibLocation = scrapy.Field()
    exhibIntro = scrapy.Field() # 展览简介


class educationItem(scrapy.Item):
    museumID = scrapy.Field() # 博物馆ID，表中自带字段，可不爬
    eduID = scrapy.Field() # 教育ID，可不爬
    eduName = scrapy.Field() # 教育活动名称
    # eduTime = scrapy.Field()
    eduContent = scrapy.Field() # 教育活动简介
    eduImg = scrapy.Field() # 教育活动图片
    # eduUrl = scrapy.Field()

    
