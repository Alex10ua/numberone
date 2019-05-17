import scrapy
from scrapy import Selector
from scrapy import Spider

from numberone.items import HotlineItem

class Hotline_spider(Spider):
    name = "Hot_Xiomi"
    start_urls = ['https://hotline.ua/mobile/mobilnye-telefony-i-smartfony/294391/']

    def parse(self, response):
        root =Selector(response)
        smartphone = root.xpath('//div[@class="tile-viewbox"]//ul[@class="products-list cell-list"]')
        for info in smartphone:
            item = HotlineItem()
            item['Hot_name']=info.xpath('//li[@class="product-item"]//div[@class="item-info"]/p[@class="h4"]//a/text()').extract() #?
            item['Hot_price']=info.xpath('//li[@class="product-item"]//div[@class="item-price stick-bottom"]//div[@class="stick-pull cell-xs-6"]//div[@class="price-md"]//span[@class="value"]/text()').extract()
            item['Hot_lowest_price_and_highest_price']=info.xpath('//li[@class="product-item"]//div[@class="item-price stick-bottom"]//div[@class="stick-pull cell-xs-6"]//div[@class="text-sm"]/text()').extract()

            yield item
