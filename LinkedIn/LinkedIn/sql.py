#coding=utf-8

import MySQLdb
from settings import MYSQL_CONFIG


MYSQL_HOST = MYSQL_CONFIG['MYSQL_HOST']
MYSQL_USER = MYSQL_CONFIG['MYSQL_USER']
MYSQL_PASSWD = MYSQL_CONFIG['MYSQL_PASSWD']
MYSQL_PORT = MYSQL_CONFIG['MYSQL_PORT']
MYSQL_DB = MYSQL_CONFIG['MYSQL_DB']

cnx = MySQLdb.connect(user=MYSQL_USER, passwd=MYSQL_PASSWD, host=MYSQL_HOST, db=MYSQL_DB, port=MYSQL_PORT, charset='utf8')
cur = cnx.cursor()

class Sql:
	
	@classmethod
	def insert_baseitem(self, id, cname, url, maidenname, fullname, summary, locationname, industryname, headline, skills, languages):
		sql = 'INSERT INTO baseitem (ID, CNAME, URL, MAIDENNAME, FULLNAME, SUMMARY, LOCATIONNAME, INDUSTRYNAME, HEADLINE, SKILLS, LANGUAGES) VALUES (%(id)s, %(cname)s, %(url)s, %(maidenname)s, %(fullname)s, %(summary)s, %(locationname)s, %(industryname)s, %(headline)s, %(skills)s, %(languages)s )'
		value = {
			'id' : id,
			'cname' : cname,
			'url' : url,
			'maidenname' : maidenname,
			'fullname' : fullname,
			'summary' : summary,
			'locationname' : locationname,
			'industryname' : industryname,
			'headline' : headline,
			'skills' : skills,
			'languages' : languages,
			}
		cur.execute(sql, value)
		cnx.commit()
	
	@classmethod
	def insert_eduitem(self, id, school, grade, degree, description, activities, fieldofstudy, start_date, end_date):
		sql = 'INSERT INTO eduitem (ID, SCHOOL, GRADE, DEGREE, DESCRIPTION, ACTIVITIES, FIELDOFSTUDY, START_DATE, END_DATE) VALUES (%(id)s, %(school)s , %(grade)s, %(degree)s, %(description)s, %(activities)s, %(fieldofstudy)s, %(start_date)s, %(end_date)s )'
		value = {
			'id' : id,
			'school' : school,
			'grade' : grade,
			'degree' : degree,
			'description' : description,
			'activities' : activities,
			'fieldofstudy' : fieldofstudy,
			'start_date' : start_date,
			'end_date'  : end_date,
			}
		cur.execute(sql, value)
		cnx.commit()

	@classmethod
	def insert_workitem(self, id, company, title, location, description, start_date, end_date):
		sql = 'INSERT INTO workitem (ID, COMPANY, TITLE, LOCATION, DESCRIPTION, START_DATE, END_DATE) VALUES (%(id)s, %(company)s, %(title)s, %(location)s, %(description)s, %(start_date)s, %(end_date)s )'
		value = {
			'id' : id,
			'company' : company,
			'title' : title,
			'location' : location,
			'description' : description,
			'start_date' : start_date,
			'end_date' : end_date,
			}
		cur.execute(sql, value)
		cnx.commit()

	@classmethod
	def insert_honoritem(self, id, issuer, title, description, start_date):
		sql = 'INSERT INTO honoritem (ID, ISSUER, TITLE, DESCRIPTION, START_DATE) VALUES (%(id)s, %(issuer)s, %(title)s, %(description)s, %(start_date)s )'
		value = {
			'id' : id,
			'issuer' : issuer,
			'title' : title,
			'description' : description,
			'start_date' : start_date,
			}
		cur.execute(sql, value)
		cnx.commit()

	@classmethod
	def insert_orgitem(self, id, name, position, start_date, end_date):
		sql = 'INSERT INTO orgitem (ID, NAME, POSITION, START_DATE, END_DATE) VALUES (%(id)s, %(name)s, %(position)s , %(start_date)s , %(end_date)s )'
		value = {
			'id' : id,
			'name' : name,
			'position' : position,
			'start_date' : start_date,
			'end_date' : end_date,
			}
		cur.execute(sql, value)
		cnx.commit()

	@classmethod
	def insert_proitem(self, id, title, description, url, start_date, end_date):
		sql = 'INSERT INTO proitem (ID, TITLE, DESCRIPTION, URL, START_DATE, END_DATE) VALUES (%(id)s, %(title)s, %(description)s, %(url)s, %(start_date)s, %(end_date)s )'
		value = {
			'id' : id,
			'title' : title,
			'description' : description,
			'url' : url,
			'start_date' : start_date,
			'end_date' : end_date,
			}
		cur.execute(sql, value)
		cnx.commit()

	@classmethod
	def insert_pubitem(self, id, publisher, description, url, name, start_date):
		sql = 'INSERT INTO pubitem (ID, PUBLISHER, DESCRIPTION, URL, NAME, START_DATE) VALUES (%(id)s, %(publisher)s, %(description)s, %(url)s, %(name)s, %(start_date)s )'
		value = {
			'id' : id,
			'publisher' : publisher,
			'description' : description,
			'url' : url,
			'name' : name,
			'start_date' : start_date,
			}
		cur.execute(sql, value)
		cnx.commit()

	@classmethod
	def insert_testitem(self, id, name, description, score, start_date):
		sql = 'INSERT INTO testitem (ID, NAME, DESCRIPTION, SCORE, START_DATE) VALUES (%(id)s, %(name)s, %(description)s, %(score)s, %(start_date)s )'
		value = {
			'id' : id,
			'name' : name,
			'description' : description,
			'score' : score,
			'start_date' : start_date,
			}
		cur.execute(sql, value)
		cnx.commit()

	@classmethod
	def insert_certitem(self, id, name, authority, licensenumber, start_date, end_date):
		sql = 'INSERT INTO certitem (ID, NAME, AUTHORITY, LICENSENUMBER, START_DATE, END_DATE) VALUES (%(id)s, %(name)s, %(authority)s, %(licensenumber)s, %(start_date)s, %(end_date)s )'
		value = {
			'id' : id,
			'name' : name,
			'authority' : authority,
			'licensenumber' : licensenumber,
			'start_date' : start_date,
			'end_date' : end_date,
			}
		cur.execute(sql, value)
		cnx.commit()
