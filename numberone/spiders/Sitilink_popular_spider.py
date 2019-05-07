import scrapy
from scrapy import Selector
from scrapy import Spider

from numberone import items
from numberone.items import EkItem


class SitilinkSpider (Spider):
    name = 'SitilinkPopular'
    start_urls=['https://sintetiki.net/most-popular/7/']

    def parse(self, response):
            #root = Selector(response)
            #smartphone=root.xpath('//div[@class="product_item_block product_item_block_full price_change_container"]')
            #for info in smartphone:
                S=items.Loader(item=items.Loader(), response=response)

                S.add_xpath('SitiPhoneName','//div[@class="product_item_title"]//a/text()')
                S.add_xpath('SitiPhonePrice','//div[@class="product_item_change"]//div[@class="product_item_btn "]/text()')
                if S.get_output_value('SitiPhonePrice')==[]:
                    S.add_xpath('SitiPhonePrice','//div[@class="product_item_change"]//div[@class="product_item_btn product_item_btn_red"]/text()')
                elif S.get_output_value('SitiPhonePrice')==[]:
                    S.add_xpath('SitiPhonePrice','//div[@class="product_item_change"]//div[@class="product_item_btn product_item_btn_green"]/text()')
                S.add_xpath('SitiPhonePriceChanged','//div[@class="product_item_change"]//div[@class="product_item_change_txt text-danger"]/text()')
                if S.get_output_value('SitiPhonePriceChanged')==[]:
                    S.add_xpath('SitiPhonePriceChanged','//div[@class="product_item_change"]//div[@class="product_item_change_txt text-success"]/text()')
                elif S.get_output_value('SitiPhonePriceChanged')==[]:
                    S.add_xpath('SitiPhonePriceChanged',[])


                #item['SitiPhoneName']=info.xpath('//div[@class="product_item_title"]//a/text()').extract()

                #item['SitiPhonePrice']=info.xpath('//div[@class="product_item_change"]//div[@class="product_item_btn product_item_btn_red"]/text()').extract()
                #item['SitiPhonePrice']=info.xpath('//div[@class="product_item_change"]//div[@class="product_item_btn "]/text()').extract()
                #item['SitiPhonePrice']=info.xpath('//div[@class="product_item_change"]//div[@class="product_item_btn product_item_btn_green"]/text()').extract()


                # if not item['SitiPhonePrice']:
                #     item['SitiPhonePrice']=info.xpath('//div[@class="product_item_change"]//div[@class="product_item_btn "]/text()').extract()
                # elif not item['SitiPhonePrice']:
                #     item['SitiPhonePrice']=info.xpath('//div[@class="product_item_change"]//div[@class="product_item_btn product_item_btn_green"]/text()').extract()
                #

                #if item['SitiPhonePriceChanged'].get_output_value('SitiPhonePriceChanged'):
                #item['SitiPhonePriceChanged']=info.xpath('//div[@class="product_item_change"]//div[@class="product_item_change_txt text-danger"]/text()').extract()
                #item['SitiPhonePriceChanged']=info.xpath('//div[@class="product_item_change"]//div[@class="product_item_change_txt text-success"]/text()').extract()
               ## if item.SitiPhonePriceChanged is None:
                #      item.SitiPhonePriceChanged="0"



                #item['SitiPhonePriceChanged']=info.xpath('//div[@class="product_item_change"]//div[@class="product_item_change_txt text-danger"]/text()').extract()


                #if not item['SitiPhonePriceChanged']:
                #    item['SitiPhonePriceChanged']=info.xpath('//div[@class="product_item_change"]//div[@class="product_item_change_txt text-success"]/text()').extract()
                #elif item['SitiPhonePriceChanged']:
                #    item['SitiPhonePriceChanged']=None
                #item['SitiAll']=info.xpath('//div[@class="product_item"]//div[@class="product_item_change"]/text()').extract()

                yield S.load_item()
# scrapy crawl name of spider
#scrapy shell 'https://scrapy.org' =>response.xpath('//title/text()').get()