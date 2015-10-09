#!/usr/bin/env python
#-*- coding: utf-8 -*-

import urllib2
import re

class scrapy:
	def gethtml(url):
		htmltext = urllib2.urlopen(url).read()
		return htmltext


class flyertea(scrapy):
			
