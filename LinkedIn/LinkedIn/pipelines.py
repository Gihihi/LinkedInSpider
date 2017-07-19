# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sql import Sql
from twisted.internet.threads import deferToThread
from items import BaseItem, EduItem, WorkItem, HonorItem, OrgItem, ProItem, PubItem, TestItem, CertItem

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
		if isinstance(item, ProItem):
			id = item['id']
			title = item['title']
			description = item['description']
			url = item['url']
			start_date = item['start_date']
			end_date = item['end_date']
			try:
				Sql.insert_proitem(id, title, description, url, start_date, end_date)
			except:
				pass
		if isinstance(item, PubItem):
			id = item['id']
			publisher = item['publisher']
			description = item['description']
			url = item['url']
			name = item['name']
			start_date = item['start_date']
			try:
				Sql.insert_pubitem(id, publisher, description, url, name, start_date)
			except:
				pass
		if isinstance(item, TestItem):
			id = item['id']
			name = item['name']
			description = item['description']
			score = item['score']
			start_date = item['start_date']
			try:
				Sql.insert_testitem(id, name, description, score, start_date)
			except:
				pass
		if isinstance(item, CertItem):
			id = item['id']
			name = item['name']
			authority = item['authority']
			licensenumber = item['licensenumber']
			start_date = item['start_date']
			end_date = item['end_date']
			try:
				Sql.insert_certitem(id, name, authority, licensenumber, start_date, end_date)
			except:
				pass
