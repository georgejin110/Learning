#!/usr/bin/env python
#-*- coding: utf-8 -*-

import urllib2, re
from bs4 import BeautifulSoup

def gethtml(url):
	headers = {
		'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
		}
	req = urllib2.Request(url, headers=headers)
	content = urllib2.urlopen(req).read()
	content = BeautifulSoup(content)
	return content

class cgbchina_crawler(object):

	def cgbchina(self, cgbchina_url):
		content = gethtml(cgbchina_url)
		print content


			
