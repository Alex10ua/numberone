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
                # item['LowPrice']=info.xpath('/html/body/div[7]/table/tbody/tr/td[1]/table/tbody/tr/td[2]/div/div/a/div/span[1]/text()').extract()
                #item['HighPrice']=info.xpath('/html/body/div[7]/table/tbody/tr/td[1]/table/tbody/tr/td[2]/div/div/a/div/span[2]').extract()
                #item['DiapasonofPrice']=('//div[@class="desc-big-price ib"]')
                #item['NameShop']=()
                #item['CurrencyofPrice']=('/html/body/div[7]/table/tbody/tr/td[1]/table/tbody/tr/td[2]/div/div/a/div/span[3]').extract()
                yield item

###scrapy crawl Phone -o  smartInformation.csv -t csv
####scrapy crawl Phone -o info.json
