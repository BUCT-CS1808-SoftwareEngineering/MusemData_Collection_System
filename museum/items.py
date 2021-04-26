# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MuseumItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    museumID = scrapy.Field()
    museumName = scrapy.Field()
    introduction = scrapy.Field()
    time = scrapy.Field() 
    # opentime=scrapy.Field()
    museumLink = scrapy.Field()
    location = scrapy.Field()
    communication = scrapy.Field()
    # latiLong = scrapy.Field()

class collectionItem(scrapy.Item):
    museumID = scrapy.Field()
    collectionID = scrapy.Field()
    collectionName = scrapy.Field()
    collectionIntroduction = scrapy.Field()
    collectionImage = scrapy.Field()#图片链接

class exhibitionItem(scrapy.Item):
    museumID = scrapy.Field()
    exhibID = scrapy.Field()
    exhibName = scrapy.Field()
    exhibTime = scrapy.Field()
    exhibLocation = scrapy.Field()
    exhibIntro = scrapy.Field()

    
