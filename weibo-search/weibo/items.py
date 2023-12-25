# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeiboItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    bid = scrapy.Field()
    userid = scrapy.Field()
    screenname = scrapy.Field()
    text = scrapy.Field()
    articleurl = scrapy.Field()
    location = scrapy.Field()
    atusers = scrapy.Field()
    topics = scrapy.Field()
    repostscount = scrapy.Field()
    commentscount = scrapy.Field()
    attitudescount = scrapy.Field()
    createdat = scrapy.Field()
    source = scrapy.Field()
    pics = scrapy.Field()
    videourl = scrapy.Field()
    retweetid = scrapy.Field()
    ip = scrapy.Field()
