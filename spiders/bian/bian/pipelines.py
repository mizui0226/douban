# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import urllib.request


class BianPipeline(object):
    def process_item(self, item, spider):
        obj = dict(item)
        dir_path = './img'
        suffix = os.path.splitext(obj['img_url'])[-1]
        file_name = obj['img_name'] + suffix
        file_path = os.path.join(dir_path,file_name)
        urllib.request.urlretrieve(obj['img_url'],file_path)
        return item
