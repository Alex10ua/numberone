# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader


class EkItem(scrapy.Item):
    Title = scrapy.Field()
    MemorySize=scrapy.Field()
    LowPrice=scrapy.Field()
    HighPrice=scrapy.Field()
    CurrencyofPrice=scrapy.Field()
    ShopsName1= scrapy.Field()
    ShopsName2= scrapy.Field()
    ShopsName3= scrapy.Field()
    ShopsName4= scrapy.Field()
    ShopsName5= scrapy.Field()
    ShopsName1Price=scrapy.Field()
    ShopsName2Price=scrapy.Field()
    ShopsName3Price=scrapy.Field()
    ShopsName4Price=scrapy.Field()
    ShopsName5Price=scrapy.Field()
    ShopsName1Discription=scrapy.Field()
    ShopsName2Discription=scrapy.Field()
    ShopsName3Discription=scrapy.Field()
    ShopsName4Discription=scrapy.Field()
    ShopsName5Discription=scrapy.Field()

    Shop1_array=scrapy.Field()
    Shop2_array=scrapy.Field()
    Shop3_array=scrapy.Field()
    Shop4_array=scrapy.Field()
    Shop5_array=scrapy.Field()

    AllProductName1=scrapy.Field()
    AllProductLowPrice1=scrapy.Field()
    AllProductHighPrice1=scrapy.Field()
    AllProductShopName1=scrapy.Field()
    AllProductShopPrice1=scrapy.Field()
    AllProductTAG=scrapy.Field()
    pass
class SitiPhone(scrapy.Item):
    SitiPhoneName=scrapy.Field()
    SitiPhonePrice=scrapy.Field()
    SitiPhonePriceChanged=scrapy.Field()
    SitiAll=scrapy.Field()

    # ShopUrl=scrapy.Field()
    pass

class Loader(ItemLoader):
    default_item_class = SitiPhone
