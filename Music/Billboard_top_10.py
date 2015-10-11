#!/usr/bin/env python
#-*- coding: utf-8 -*-

import urllib2, re

def gethtml(url):
	headers = {
		'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
	}
	req = urllib2.Request(url, headers=headers)
	content = urllib2.urlopen(req).read()
	return content

def getinfo():
	this_week = re.compile(r'<span class="this-week">"(\d)"</span>')
	this_week_number = re.findall(this_week,gethtml(billboard_url))
	return this_week_number

billboard_url = "http://www.billboard.com/charts/hot-100"

# print gethtml(billboard_url)
print getinfo()