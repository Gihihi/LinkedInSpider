# -*- coding: utf-8 -*-
import scrapy
import MySQLdb
import random
import re
import json
from LinkedIn.items import BaseItem, EduItem, WorkItem
from cookie import cookie
from LinkedIn.settings import MYSQL_CONFIG


MYSQL_HOST = MYSQL_CONFIG['MYSQL_HOST']
MYSQL_USER = MYSQL_CONFIG['MYSQL_USER']
MYSQL_PASSWD = MYSQL_CONFIG['MYSQL_PASSWD']
MYSQL_PORT = MYSQL_CONFIG['MYSQL_PORT']
MYSQL_DB = MYSQL_CONFIG['MYSQL_DB']

cnx = MySQLdb.connect(user=MYSQL_USER, passwd=MYSQL_PASSWD, host=MYSQL_HOST, db=MYSQL_DB, port=MYSQL_PORT, charset='utf8')
cur = cnx.cursor()

#待爬池获取个人信息
cur.execute('select distinct id, cname from person_url')

#指定本次爬去数量
#rows = cur.fetchall()
#rows = cur.fetchmany(4000)
rows = cur.fetchmany(5)

cur.close

COOKIES = cookie

class GetPersonInfoSpider(scrapy.Spider):
	name = 'get_person_info'
	allowed_domains = ['www.linkedin.com']
	start_urls = ['https://www.linkedin.com/']

	start_url = 'https://www.linkedin.com/in/'

	def start_requests(self):
		for row in rows:
			url = self.start_url + row[0]
			yield scrapy.Request(url, cookies=COOKIES, callback=self.parse, meta={'id' : row[0], 'cname' : row[1]})

	def parse(self, response):
		content = response.body.replace('&quot;', '"')
		
		id = response.meta['id']
		cname = response.meta['cname']
		url = response.url

		#基本信息-信息
		item = BaseItem()
		Profile = re.findall('\{[^\{]*?"com\.linkedin\.voyager\.identity\.profile\.Profile"[^\}]*?\}', content)[0]
		Profile_info = json.loads(Profile)
		item['id'] = id
		item['cname'] = cname
		item['url'] = url
		item['maidenname'] = Profile_info.get('maidenName','')
		item['fullname'] = Profile_info.get('lastName','') + Profile_info.get('firstName','')
		item['summary'] = Profile_info.get('summary','')
		item['locationname'] = Profile_info.get('locationName','')
		item['industryname'] = Profile_info.get('industryName','')
		item['headline'] = Profile_info.get('headline','')
		#基本信息-语言
		Language_list = re.findall('\{[^\{]*?"com\.linkedin\.voyager\.identity\.profile\.Language"[^\}]*?\}', content)
		Languages = []
		for Language in Language_list:
			Language_info = json.loads(Language)
			Languages.append(Language_info.get('name', '') + ':' + Language_info.get('proficiency', '-'))
		item['languages'] = ','.join(Languages)
		#基本信息-技能
		Skill_list = re.findall('\{[^\{]*?"com\.linkedin\.voyager\.identity\.profile\.Skill"[^\}]*?\}', content)
		Skills = []
		for Skill in Skill_list:
			Skill_info = json.loads(Skill)
			Skills.append(Skill_info['name'])
		item['skills'] = ','.join(Skills)
		yield item

		#教育经历
		Education_list = re.findall('\{[^\{]*?"com\.linkedin\.voyager\.identity\.profile\.Education"[^\}]*?\}', content)
		for Education in Education_list:
			item = EduItem()
			Education_info = json.loads(Education)
			item['id'] = id
			item['activities'] = Education_info.get('activities','')
			item['description'] = Education_info.get('description','')
			item['school'] = Education_info.get('schoolName','')
			item['grade'] = Education_info.get('grade','')
			item['degree'] = Education_info.get('degreeName','')
			item['fieldofstudy'] = Education_info.get('fieldOfStudy','')
			start_Date_json = json.loads(re.findall('\{[^\{]*?"\$id":"%s,startDate"[^\}]*?\}' % Education_info.get('timePeriod','').replace('(', '\(').replace(')', '\)'), content)[0])
			start_date = str(start_Date_json.get('year','-')) + '-' + str(start_Date_json.get('month','/')) + '-' + str(start_Date_json.get('day','/'))
			item['start_date'] = start_date.replace('-/', '')
			try:
				end_Date_json = json.loads(re.findall('\{[^\{]*?"\$id":"%s,endDate"[^\}]*?\}' % Education_info.get('timePeriod','').replace('(', '\(').replace(')', '\)'), content)[0])
				end_date = str(end_Date_json.get('year','-')) + '-' + str(end_Date_json.get('month','/')) + '-' + str(end_Date_json.get('day','/'))
				item['end_date'] = end_date.replace('-/', '')
			except:
				item['end_date'] = '至今'
			yield item

		#工作经历
		Position_list = re.findall('\{[^\{]*?"com\.linkedin\.voyager\.identity\.profile\.Position"[^\}]*?\}', content)
		for Position in Position_list:
			item = WorkItem()
			Position_info = json.loads(Position)
			item['id'] = id
			item['description'] = Position_info.get('description','')
			item['company'] = Position_info.get('companyName','')
			item['title'] = Position_info.get('title','')
			item['location'] = Position_info.get('locationName','')
			start_Date_json = json.loads(re.findall('\{[^\{]*?"\$id":"%s,startDate"[^\}]*?\}' % Position_info.get('timePeriod','').replace('(', '\(').replace(')', '\)'), content)[0])
			start_date = str(start_Date_json.get('year','-')) + '-' + str(start_Date_json.get('month','/')) + '-' + str(start_Date_json.get('day','/'))
			item['start_date'] = start_date.replace('-/', '')
			try:
				end_Date_json = json.loads(re.findall('\{[^\{]*?"\$id":"%s,endDate"[^\}]*?\}' % Position_info.get('timePeriod','').replace('(', '\(').replace(')', '\)'), content)[0])
				end_date = str(end_Date_json.get('year','-')) + '-' + str(end_Date_json.get('month','/')) + '-' + str(end_Date_json.get('day','/'))
				item['end_date'] = end_date.replace('-/', '')
			except:
				item['end_date'] = '至今'
			yield item
