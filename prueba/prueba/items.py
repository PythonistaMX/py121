# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class PruebaItem(Item):
    # Primary fields
    platillo = Field()
    precio = Field()
