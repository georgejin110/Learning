#!/usr/bin/env python
#-*- coding: utf-8 -*-

import urllib2
import sys
import re

def gethtml(url):
	htmlfile = urllib2.urlopen(url)
	htmltext = htmlfile.read()
	return htmltext