import scrapy
from scrapy import Selector
from scrapy import Spider

from numberone.items import EkItem


class SitilinkSpider (Spider):
    name = 'SitilinkPopular'
    start_urls=['https://sintetiki.net/most-popular/7/']

    def parse(self, response):
            root = Selector(response)
            smartphone=root.xpath('//div[@class="product_item_block product_item_block_full price_change_container"]')
            for info in smartphone:
                item=EkItem()

                item['SitiPhoneName']=info.xpath('//div[@class="product_item_title"]//a/text()').extract()

                item['SitiPhonePrice']=info.xpath('//div[@class="product_item_change"]//div[@class="product_item_btn product_item_btn_red"]/text()').extract()
                item['SitiPhonePrice']=info.xpath('//div[@class="product_item_change"]//div[@class="product_item_btn "]/text()').extract()
                item['SitiPhonePrice']=info.xpath('//div[@class="product_item_change"]//div[@class="product_item_btn product_item_btn_green"]/text()').extract()


                # if not item['SitiPhonePrice']:
                #     item['SitiPhonePrice']=info.xpath('//div[@class="product_item_change"]//div[@class="product_item_btn "]/text()').extract()
                # elif not item['SitiPhonePrice']:
                #     item['SitiPhonePrice']=info.xpath('//div[@class="product_item_change"]//div[@class="product_item_btn product_item_btn_green"]/text()').extract()
                #
                item['SitiPhonePriceChanged']=info.xpath('//div[@class="product_item_change"]//div[@class="product_item_change_txt text-danger"]/text()').extract()
                item['SitiPhonePriceChanged']=info.xpath('//div[@class="product_item_change"]//div[@class="product_item_change_txt text-success"]/text()').extract()
               ## if item.SitiPhonePriceChanged is None:
                #      item.SitiPhonePriceChanged="0"



                #item['SitiPhonePriceChanged']=info.xpath('//div[@class="product_item_change"]//div[@class="product_item_change_txt text-danger"]/text()').extract()


                #if not item['SitiPhonePriceChanged']:
                #    item['SitiPhonePriceChanged']=info.xpath('//div[@class="product_item_change"]//div[@class="product_item_change_txt text-success"]/text()').extract()
                #elif item['SitiPhonePriceChanged']:
                #    item['SitiPhonePriceChanged']=None
                #item['SitiAll']=info.xpath('//div[@class="product_item"]//div[@class="product_item_change"]/text()').extract()

                yield  item
