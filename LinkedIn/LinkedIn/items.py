# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class BaseItem(scrapy.Item):
	
	#基本信息
	id = scrapy.Field()
	cname = scrapy.Field()
	url = scrapy.Field()
	maidenname = scrapy.Field()
	fullname = scrapy.Field()
	summary = scrapy.Field()
	locationname = scrapy.Field()
	industryname = scrapy.Field()
	headline = scrapy.Field()
	skills = scrapy.Field()
	languages = scrapy.Field()
