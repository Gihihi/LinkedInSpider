# -*- coding: utf-8 -*-
import scrapy
import re
from whitelist import WHITE_LIST


class LinkedinSpider(scrapy.Spider):
	name = "linkedin"
	allowed_domains = ["linkedin.com"]
	start_urls = (
		'http://www.linkedin.com/feed/',
	)
	bash_url = 'http://www.linkedin.com/'
	person_url = 'http://www.linkedin.com/in/'
	start_url = 'http://www.linkedin.com/search/results/people/?keywords='
	end_url = '&page='
	

	def parse(self, response):
		'''
			根据关键字进行搜索
		'''
		for key_word in KEY_WORDS:
			url = self.start_url + key_word
			yield scrapy.Request(url, cookies=self.cookies, callback=self.parse_page, meta={'key_word' : key_word})

	def parse_page(self, response):
		'''
			翻页处理
		'''
		for i in range(1, 2):
			url = self.start_url + response.meta['key_word'] + self.end_url + str(i)
			yield scrapy.Request(url, cookies=self.cookies, callback=self.parse_person_url)

	def parse_person_url(self, response):
		'''
			解析非好友个人主页url
		'''
		pattern = re.compile('.*?&quot;publicIdentifier&quot;:&quot;(.*?)&quot;.*?', re.S)
		items = re.findall(pattern, response.body)
		for item in items:
			if item not in WHITE_LIST: 
				url = self.person_url +  item
				yield scrapy.Request(url, cookies=self.cookies, callback=self.parse_person_info)
	
	def parse_person_info(self, response):
		'''
			解析LinkedIn个人主页
		'''
		content = response.body.replace('&quot;', '"')
		profile_txt = ' '.join(re.findall('\{[^\{]*?profile\.Profile"[^\}]*?\}', content))
		firstName = re.findall('"firstName":"(.*?)"', profile_txt)
		lastName = re.findall('"lastName":"(.*?)"', profile_txt)

		if firstName and lastName:
			print '姓名: %s%s LinkedIn: %s' %(lastName[0], firstName[0], response.url)
