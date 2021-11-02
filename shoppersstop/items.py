# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ShoppersstopItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    url = scrapy.Field()
    price = scrapy.Field()
    brand = scrapy.Field()
    imageUrl1 = scrapy.Field()
    imageUrl2 = scrapy.Field()
    
