# -*- coding: utf-8 -*-
import scrapy
import re

WHITE_LIST = [
        'milagros-zhang-6ba21b126',
        'jackwang1234',
        '超庭-吴-79b002129',
        'hunter-ella',
        '晨曦-张-a0b863a0',
        '伟楠-岂-6bb189bb',
        'gina-dong-668b06102',
        '茜茜-芦-006687118',
        '云秀-孟-8b5a92100',
        '世昕-宋-429b46ab',
        'leu-karen-512b03120',
        'cecilia-wu-126994102',
        '彦龙-张-7b2b62110',
        '静达-明-b16963126',
        '彦龙-张-4485a9b2',
        '千里-马-12b5b9129',
        ]


class LinkedinSpider(scrapy.Spider):
    name = "linkedin"
    allowed_domains = ["linkedin.com"]
    start_urls = (
        'http://www.linkedin.com/feed/',
    )
    bash_url = 'http://www.linkedin.com/'
    
    start_url = 'http://www.linkedin.com/search/results/index/?keywords=小米&page='
    cookies = {
        'JSESSIONID' : '"ajax:0183095991136748236"',
        '_lipt' : 'CwEAAAFcs_B_PfbmSHBt-HoQu1SiodBIvkTk_z77oP8kRnR5OOBbpyg1Adzpwz56kXyTk9chTmoJ3aJ2lQp6IxhAxym5vflHXB3k60ss7l7UKHEZyIVE06TRHLwtjfSd1g_42eLA8pCU25idM-1jRvuQYSHrwHucz2vPfgjaUJQc-jG5sSowSnPreUqcDfWCp3TKWWehgw',
        'bcookie' : '"v=2&44209652-16bd-4c25-80d9-f09440b5658a"',
        'lang' : '"v=2&lang=zh-cn"',
        'li_at' : 'AQEDAR-XRHMAvfmTAAABXLPi79UAAAFctZpj1VEAYlcOZEdGSgSg2dbWRw2H-zz3cHXwVndIeRysqcDQtfe1hS3vFpkio_WELqm_qyEsiPRSChd1Sy7uwFv5A0mgyWTf-P2heut5P3Y_y6mBS67ToCzF',
        'liap' : 'true',
        'lidc' : '"b=SB55:g=17:u=4:i=1497666613:t=1497713043:s=AQGiuCQ_aaGwDfOu-WqBD4Zqyljo5GWI"',
        'sdsc' : '1%3A1SZM1shxDNbLt36wZwCgPgvN58iw%3D',
        'visit' : '"v=1&M"',
        'wwepo' : 'true',
            }

    def parse(self, response):
        for i in range(1, 6):
            url = self.start_url + str(i)
            yield scrapy.FormRequest(url, cookies=self.cookies, callback=self.parse_page)

    def parse_page(self, response):
        pattern = re.compile('.*?&quot;publicIdentifier&quot;:&quot;(.*?)&quot;.*?', re.S)
        items = re.findall(pattern, response.body)
        url_list = []
        print ('==========================================================')
        for item in items:
            if item not in WHITE_LIST: 
                url_list.append(self.bash_url + 'in/' +  item)
        print(url_list)
        print ('==========================================================')
        
        
        #with open('result.html', 'w') as filename:
        #    filename.write(response.body)
        #print ('==========================================================')
        #print response.url
        #print ('==========================================================')
        #name_list = response.xpath('//span[@class="name actor-name"]/text()').extract()
        #a = response.xpath('//*[@id="ember3406"]/span[1]').extract()
        #print('================================')
        #print(a)
       
