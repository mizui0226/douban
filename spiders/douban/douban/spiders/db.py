# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from douban.items import DoubanItem


class DbSpider(CrawlSpider):
    name = 'db'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    rules = (
        Rule(LinkExtractor(allow=r'.*?start=+\d+&filter='), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        li_list = response.xpath('//div[@id="content"]/div[@class="grid-16-8 clearfix"]/div[@class="article"]/ol[@class="grid_view"]//li')
        for li in li_list:
            item = DoubanItem()
            item['movie_name'] = li.xpath('.//div/div[@class="info"]/div[@class="hd"]/a/span[1]/text()').extract_first()
            movie_info_url = li.xpath('.//div/div[@class="info"]/div[@class="hd"]/a/@href').extract_first()
            yield scrapy.Request(url=movie_info_url,callback=self.movie_info,meta={'item':item})

    def movie_info(self,response):
        item = response.meta['item']
        item['movie_img'] = response.xpath('//div[@id="mainpic"]/a/img/@src').extract_first()
        item['movie_director'] = response.xpath('//div[@id="info"]/span[1]/span[@class="attrs"]/a/text()').extract_first()
        item['movie_actor'] = response.xpath('//div[@id="info"]/span[@class="actor"]//span//a/text()').extract_first()
        item['movie_top'] = response.xpath('//div[@id="content"]/div[@class="top250"]/span/text()').extract_first()
        item['movie_type'] = response.xpath('//div[@id="info"]//span[@property="v:genre"]/text()').extract_first()
        item['movie_date'] = response.xpath('//div[@id="info"]//span[@property="v:initialReleaseDate"]/text()').extract_first()
        item['movie_time'] = response.xpath('//div[@id="info"]//span[@property="v:runtime"]/text()').extract_first()
        item['movie_info'] = response.xpath('//div[@id="link-report"]/span[@class="short"]/span[@property="v:summary"]/text()').extract_first()
        yield item