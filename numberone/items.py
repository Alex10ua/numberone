# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EkItem(scrapy.item):
    #url = scrapy.Field()
    Title = scrapy.Field()
    #NameShop= scrapy.Field()
    #ShopUrl=scrapy.Field()
    #DiapasonofPrice=scrapy.Field()
    LowPrice=scrapy.Field()
    HighPrice=scrapy.Field()
    CurrencyofPrice=scrapy.Field()
    #PriceofPhoneInShop=scrapy.Field()
    pass