# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

# import scrapy
from scrapy.item import Item, Field


class PropertiesItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # Primary fields
    title = Field()
    url = Field()
    img_url = Field()
    student = Field()
    introduction = Field()
    image_path = Field()

    # pass
