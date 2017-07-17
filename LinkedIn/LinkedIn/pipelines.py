# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sql import Sql
from twisted.internet.threads import deferToThread
from items import BaseItem

class LinkedinPipeline(object):
    
	def process_item(self, item, spider):
		if isinstance(item, BaseItem):
			id = item['id'] 
			cname = item['cname']
			url = item['url']
			maidenname = item['maidenname']
			fullname = item['fullname']
			summary = item['summary']
			locationname = item['locationname']
			industryname = item['industryname']
			headline = item['headline']
			skills = item['skills']
			languages = item['languages']
			Sql.insert_baseitem(id, cname, url, maidenname, fullname, summary, locationname, industryname, headline, skills, languages)

