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
                #item['AllProductShopName1']=info.xpath('/html/body/div[6]/table/tbody/tr/td[1]/form/div[1]/div[2]/table/tbody/tr/td[3]/div[2]/table/tbody/tr[1]/td[1]/div/a/u').extract()
                #item['AllProductShopPrice1']=info.xpath('//table[@class="model-short-block"]//td[@class="model-hot-prices-td"]//div[@class="l-pr-pd"]//table[@class="model-hot-prices"]//td[@class="model-shop-name"]//div[@class="sn-div"]//a/text()').extract()
                item['AllProductTAG']=info.xpath('//div[@class="model-short-description"]//div[@class="m-s-f1 no-mobile"]//a[@class="ib no-u "]/text()').extract()
                item['AllProductTAG']=info.xpath('//div[@class="model-short-description"]//div[@class="m-s-f1 no-mobile"]//a[@class="ib no-u "][2]/text()').extract()
                item['AllProductTAG']=info.xpath('//div[@class="model-short-description"]//div[@class="m-s-f1 no-mobile"]//a[@class="ib no-u "][3]/text()').extract()
                item['AllProductTAG']=info.xpath('//div[@class="model-short-description"]//div[@class="m-s-f1 no-mobile"]//a[@class="ib no-u "][4]/text()').extract()
                item['AllProductTAG']=info.xpath('//div[@class="model-short-description"]//div[@class="m-s-f1 no-mobile"]//a[@class="ib no-u "][5]/text()').extract()
                item['AllProductTAG']=info.xpath('//div[@class="model-short-description"]//div[@class="m-s-f1 no-mobile"]//a[@class="ib no-u "][6]/text()').extract()
                item['AllProductTAG']=info.xpath('//div[@class="model-short-description"]//div[@class="m-s-f1 no-mobile"]//a[@class="ib no-u "][7]/text()').extract()
                item['AllProductTAG']=info.xpath('//div[@class="model-short-description"]//div[@class="m-s-f1 no-mobile"]//a[@class="ib no-u "][8]/text()').extract()
                item['AllProductTAG']=info.xpath('//div[@class="model-short-description"]//div[@class="m-s-f1 no-mobile"]//a[@class="ib no-u "][9]/text()').extract()
                item['AllProductTAG']=info.xpath('//div[@class="model-short-description"]//div[@class="m-s-f1 no-mobile"]//a[@class="ib no-u "][10]/text()').extract()
                item['AllProductTAG']=info.xpath('//div[@class="model-short-description"]//div[@class="m-s-f1 no-mobile"]//a[@class="ib no-u "][11]/text()').extract()
                item['AllProductTAG']=info.xpath('//div[@class="model-short-description"]//div[@class="m-s-f1 no-mobile"]//a[@class="ib no-u "][12]/text()').extract()

                yield item