# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from bian.items import BianItem


class BaSpider(CrawlSpider):
    name = 'ba'
    allowed_domains = ['pic.netbian.com']
    start_urls = ['http://pic.netbian.com/4kfengjing/']

    rules = (
        Rule(LinkExtractor(allow=r'/4kfengjing/index_\d+.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        li_list = response.xpath('//div[@id="main"]/div[@class="slist"]/ul[@class="clearfix"]//li')
        for li in li_list:
            item = BianItem()
            item['img_name'] = li.xpath('.//a/img/@alt').extract_first()
            img_info_url = 'http://pic.netbian.com' + li.xpath('.//a/@href').extract_first()
            yield scrapy.Request(url=img_info_url,callback=self.img_info,meta={'item':item})


    def img_info(self,response):
        item = response.meta['item']
        img_url_temp = response.xpath('//div[@class="view"]/div[@class="photo-pic"]/a/img/@src').extract_first()
        item['img_url'] = 'http://pic.netbian.com' + img_url_temp
        yield item



