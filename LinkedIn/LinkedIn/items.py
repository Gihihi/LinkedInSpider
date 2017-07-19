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

class EduItem(scrapy.Item):

	#教育经历
	id = scrapy.Field()
	school = scrapy.Field()
	grade = scrapy.Field()
	degree = scrapy.Field()
	description = scrapy.Field()
	activities = scrapy.Field()
	fieldofstudy = scrapy.Field()
	start_date = scrapy.Field()
	end_date = scrapy.Field()

class WorkItem(scrapy.Item):

	#工作经历
	id = scrapy.Field()
	company = scrapy.Field()
	title = scrapy.Field()
	location = scrapy.Field()
	description = scrapy.Field()
	start_date = scrapy.Field()
	end_date = scrapy.Field()

class HonorItem(scrapy.Item):

	#荣誉奖项
	id = scrapy.Field()
	issuer = scrapy.Field()
	title = scrapy.Field()
	description = scrapy.Field()
	start_date = scrapy.Field()

class OrgItem(scrapy.Item):
	
	#参与组织	
	id = scrapy.Field()
	name = scrapy.Field()
	position = scrapy.Field()
	start_date = scrapy.Field()
	end_date = scrapy.Field()

class ProItem(scrapy.Item):
	
	#项目经历
	id = scrapy.Field()
	title = scrapy.Field()
	description = scrapy.Field()
	url = scrapy.Field()
	start_date = scrapy.Field()
	end_date = scrapy.Field()

class PubItem(scrapy.Item):
	
	#出版作品
	id = scrapy.Field()
	publisher = scrapy.Field()
	description = scrapy.Field()
	url = scrapy.Field()
	name = scrapy.Field()
	start_date = scrapy.Field()

class TestItem(scrapy.Item):

	#测试成绩
	id = scrapy.Field()
	name = scrapy.Field()
	description = scrapy.Field()
	score = scrapy.Field()
	start_date = scrapy.Field()

class CertItem(scrapy.Item):
	
	#资格认证
	id = scrapy.Field()
	name = scrapy.Field()
	authority = scrapy.Field()
	licensenumber = scrapy.Field()
	start_date = scrapy.Field()
	end_date = scrapy.Field()
