from fileinput import filename

import scrapy
from pip._internal.utils import logging
from scrapy import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Spider
from scrapy import spiders
from scrapy import Spider

from numberone.items import EkItem


class eKSpider(Spider):
    name = "Phone"

    #url=['https://ek.ua/XIAOMI-MI-9-64GB.htm','https://ek.ua/list/122/xiaomi/']
    #start_urls=['https://coinmarketcap.com/ru/']
    start_urls=['https://ek.ua/XIAOMI-MI-9-64GB.htm']


    # custom_settings = {
    #    'LOG_LEVEL': logging.WARNING,
    #   'ITEM_PIPELINES':{'__main__.JsonWriterPipeline':1},
    #   'FEED_FORMAT':'json',
    #   'FEED_URI':'data.json'
    #}
    def parse(self, response):
        root =Selector(response)
        smartphone=root.xpath('//td[@class="main-part-content"]')
        for info in smartphone:
                item=EkItem()
                item['Title']=info.xpath('//h1[@class="t2 no-mobile"]/text()').extract()
                item['MemorySize']=info.xpath('//h1[@class="t2 no-mobile"]/span/text()').extract()
                item['LowPrice']=info.xpath('//div[@class="desc-big-price ib"]/span[@itemprop="lowPrice"]/text()').extract()
                item['HighPrice']=info.xpath('//div[@class="desc-big-price ib"]/span[@itemprop="highPrice"]/text()').extract()
                item['CurrencyofPrice']=info.xpath('//div[@class="desc-big-price ib"]//span[@class="desc-pr-cur"]/text()').extract()
                item['ShopsName1']=info.xpath('//tr[@class="  tr-odd"]//a[@class="it-shop"]/text()').extract()
                item['ShopsName2']=info.xpath('//tr[@class="  tr-odd"][2]//a[@class="it-shop"]/text()').extract()
                item['ShopsName3']=info.xpath('//tr[@class="  tr-odd"][3]//a[@class="it-shop"]/text()').extract()
                item['ShopsName4']=info.xpath('//tr[@class=" "]//a[@class="it-shop"]/text()').extract()
                item['ShopsName5']=info.xpath('//tr[@class=" "][2]//a[@class="it-shop"]/text()').extract()
                item['ShopsName1Price']=info.xpath('//tr[@class="  tr-odd"]/td[@class="where-buy-price"]/a/text()').extract()
                item['ShopsName2Price']=info.xpath('//tr[@class="  tr-odd"][2]/td[@class="where-buy-price"]/a/text()').extract()
                item['ShopsName3Price']=info.xpath('//tr[@class="  tr-odd"][3]/td[@class="where-buy-price"]/a/text()').extract()
                item['ShopsName4Price']=info.xpath('//tr[@class=" "]/td[@class="where-buy-price"]/a/text()').extract()
                item['ShopsName5Price']=info.xpath('//tr[@class=" "][2]/td[@class="where-buy-price"]/a/text()').extract()
                #item['ShopsName1Discription']=info.xpath('//tr[@class="  tr-odd"]//td[@class="where-buy-price"]//h3[1]/text()').extract()
                #item['ShopsName2Discription']=info.xpath('').extract()
                #item['ShopsName3Discription']=info.xpath('').extract()
                #item['ShopsName4Discription']=info.xpath('').extract()
                #item['ShopsName5Discription']=info.xpath('').extract()



                yield item

####scrapy crawl Phone -o  smartInformation.csv -t csv
####scrapy crawl Phone -o info.json
