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
