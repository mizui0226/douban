# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    movie_name = scrapy.Field()
    movie_img = scrapy.Field()
    movie_director = scrapy.Field()
    movie_actor = scrapy.Field()
    movie_top = scrapy.Field()
    movie_type = scrapy.Field()
    movie_date = scrapy.Field()
    movie_time = scrapy.Field()
    movie_info = scrapy.Field()
