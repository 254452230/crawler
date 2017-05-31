# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    index = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    content = scrapy.Field()
    tag = scrapy.Field()
    similarProblem = scrapy.Field()
    totalAccepted = scrapy.Field()
    totalSubmission = scrapy.Field()
    difficulty = scrapy.Field()
    contributor = scrapy.Field()
