# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class NumberonePipeline(object):
    def process_item(self, item, spider):
        return item

class JsonPipeline(object):
    def open_spider(self,spider):
        self.file=open('data.jl','w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self,item,spider):
        line=json.dumps(dict(item)) +"\n"
        self.file.write(line)
        return item