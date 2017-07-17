# -*- coding: utf-8 -*-
import scrapy
import re
from keyword import KEY_WORDS
from cookie import cookie

class GetUrlSpider(scrapy.Spider):
	name = 'get_url'
	allowed_domains = ['www.linkedin.com']
	start_urls = ['http://www.linkedin.com/']

	start_url = 'https://www.linkedin.com/search/results/people/?facetCurrentCompany=["'
	end_url = '"]&facetGeoRegion=["cn:0"]&page='
	
	home_path ='/home/python/GitHub/LinkedInSpider/url_info/url/'

	def start_requests(self):
		'''
			搜索关键字
		'''
		for company_id in KEY_WORDS.keys():
			for page in range(1,6):
				url = self.start_url + company_id + self.end_url + str(page)
				yield scrapy.Request(url, cookies=cookie, callback=self.parse, meta={'cid' : company_id, 'page' : str(page)})

	def parse(self, response):
		
		content = response.body
		company = KEY_WORDS[response.meta['cid']]

		with open (self.home_path + company + '/'  + response.meta['cid'] + '_' + response.meta['page'] + '.txt', 'w') as f:
			f.write(content)
