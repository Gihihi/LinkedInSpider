# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sql import Sql
from twisted.internet.threads import deferToThread
from items import BaseItem, EduItem, WorkItem, HonorItem, OrgItem

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
			try:
				Sql.insert_baseitem(id, cname, url, maidenname, fullname, summary, locationname, industryname, headline, skills, languages)
			except:
				pass
		if isinstance(item, EduItem):
			id = item['id']
			school = item['school']
			grade = item['grade']
			degree = item['degree']
			description = item['description']
			activities = item['activities']
			fieldofstudy = item['fieldofstudy']
			start_date = item['start_date']
			end_date = item['end_date']
			try:
				Sql.insert_eduitem(id, school, grade, degree, description, activities, fieldofstudy, start_date, end_date)
			except:
				pass
		if isinstance(item, WorkItem):
			id = item['id'] 
			company = item['company']
			title = item['title']
			location = item['location']
			description = item['description']
			start_date = item['start_date']
			end_date = item['end_date']
			try:
				Sql.insert_workitem(id, company, title, location, description, start_date, end_date)
			except:
				pass
		if isinstance(item, HonorItem):
			id = item['id']
			issuer = item['issuer']
			title = item['title']
			description = item['description']
			start_date = item['start_date']
			try:
				Sql.insert_honoritem(id, issuer, title, description, start_date)
			except:
				pass
		if isinstance(item, OrgItem):
			id = item['id']
			name = item['name']
			position = item['position']
			start_date = item['start_date']
			end_date = item['end_date']
			try:
				Sql.insert_orgitem(id, name, position, start_date, end_date)
			except:
				pass
