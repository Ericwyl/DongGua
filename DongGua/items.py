# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class DongguaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    targetname = scrapy.Field()
    targetid = scrapy.Field()
    targetsequence = scrapy.Field()
    targetsynonyms = scrapy.Field()
    targetsource = scrapy.Field()
    targetstructure = scrapy.Field()
    comments = scrapy.Field()
    targettype = scrapy.Field()
