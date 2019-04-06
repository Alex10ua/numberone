import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

class EkSpider(scrapy.Spider):
    name = "Ek"

    def start_requests(self):
        url=['https://ek.ua/list/122/xiaomi/']
        allowed_domains=['ek.ua']

        rule=(
            Rule(LinkExtractor(
                restrict_xpaths=['//*[@id="mr_g1tge6zf762"]/table  ']
            )
            )
        )