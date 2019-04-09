import scrapy
from pip._internal.utils import logging
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

class Spider(scrapy.Spider):
    name = "Coin"

    url=['https://coinmarketcap.com/ru/all/views/all/']
    start_urls=['https://coinmarketcap.com/ru/']

    custom_settings = {
        'LOG_LEVEL': logging.WARNING,
        'ITEM_PIPELINES':{'__main__.JsonWriterPipeline':1},
        'FEED_FORMAT':'json',
        'FEED_URI':'data.json'
    }
    def parse(self, response):
        for ood in  response.css()

