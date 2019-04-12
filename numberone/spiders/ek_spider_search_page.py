import scrapy
from scrapy import Selector
from scrapy import Spider

from numberone.items import EkItem


class ekSpiderAll (Spider):
    name = "All_phone"
    start_urls=['https://ek.ua/list/122/xiaomi/']

    def parse(self, response):
        root = Selector(response)
        smartphone = root.xpath('//td[@class="main-part-content"]')
        for info in smartphone:
                item=EkItem()
                item['AllProductName1']=info.xpath('//td[@class="model-short-info"][1]//span[@class="u"]/text()').extract()
                item['AllProductLowPrice1']=info.xpath('//div[@class="model-price-range"]//a[@title="Сравнить цены! "]//span[1]/text()').extract()
                item['AllProductHighPrice1']=info.xpath('//div[@class="model-price-range"]//a[@title="Сравнить цены! "]//span[2]/text()').extract()
                #item['AllProductShopName1']=info.xpath('//div[@class="l-pr-pd"]//td[@class="model-shop-name"]//a//u/text()').extract()
                #item['AllProductShopPrice1']=info.xpath('//div[@class="l-pr-pd"]//td[@class="model-shop-price"]//a/text()').extract()
                yield item