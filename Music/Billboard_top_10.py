#!/usr/bin/env python
#-*- coding: utf-8 -*-

import urllib2, re

def GetHTML(url):
	headers = {
		'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
	}
	req = urllib2.Request(url, headers=headers)
	content = urllib2.urlopen(req).read()
	return content

def Infomation():
	def add(x):
		return "This Week: "+x
	gethtml = GetHTML(billboard_url)
	ThisWeekList = re.findall(re.compile(r'<.+="this-week">(\d+)<.+>'), gethtml)
	ThisWeekList = map(add, ThisWeekList)
	LastWeekList = re.findall(re.compile(r'<.+="last-week">(.+)<.+>'), gethtml)
	SongName = re.findall(re.compile(r'<.+"row-title">\s+<h2>\s+(.+)\s+<\/h2>'), gethtml)
	SongNameList = ["Song: "+s.replace("&#039;", "\'") for s in SongName]
	ArtistName = re.findall(re.compile(r'<.+="Artist Name.+>\s+(.+)\s+<\/a>'), gethtml)
	ArtistNameList = ["Artist: "+a.replace("&amp;", "&") for a in ArtistName]
	zipped = zip(ThisWeekList, LastWeekList, SongNameList, ArtistNameList)
	for i in zipped:
		SongInfo = [''.join(value) for value in i]
		SongInfoStr = '    '.join(SongInfo)
		print SongInfoStr

billboard_url = "http://www.billboard.com/charts/hot-100"

Infomation()


# def Name():
# 	SongName = re.compile(r'<.+"row-title">\s+<h2>\s+(.+)\s+<\/h2>')
# 	SongName = re.findall(SongName, GetHTML(billboard_url))
# 	SongNameList = [s.replace("&#039;", "\'") for s in SongName]
# 	return SongNameList

# def artist():
# 	ArtistName = re.compile(r'<.+="Artist Name.+>\s+(.+)\s+<\/a>')
# 	ArtistName = re.findall(ArtistName, GetHTML(billboard_url))
# 	ArtistNameList = [a.replace("&amp;", "&") for a in ArtistName]
# 	return ArtistNameList	


# f = open("billboard.txt", "wb")

# # f.write(GetHTML(billboard_url))
# # f.close()
