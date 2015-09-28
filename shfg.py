#!/usr/bin/env python
#-*- coding: utf-8 -*-

import urllib2
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def getHTML(urls):
	htmlfile = urllib2.urlopen(urls)
	htmltext = htmlfile.read()
	return htmltext

def getData(urls):
	source = getHTML(urls)
	data = json.loads(source)
	xiaoqudata = data['data']
	return xiaoqudata

def address(xiaoqudata):
	try:
		return u"小区地址：", xiaoqudata['concretaddr']
	except KeyError, e:
		pass

def name(xiaoqudata):
	try:
		return u"小区名称：", xiaoqudata['projectname']
	except KeyError, e:
		pass

def wuye(xiaoqudata):
	try:
		return u"在管物业企业：", xiaoqudata['companyname']
	except KeyError, e:
		pass

def Area(xiaoqudata):
	try:
		return u"所在区县：", xiaoqudata["distname"]
	except Exception, e:
		pass

def KeyID(xiaoqudata):
	try:
		return u"小区ID：", xiaoqudata["keyid"]
	except Exception, e:
		pass

def StreetName(xiaoqudata):
	try:
		return u"所在街道：", xiaoqudata["streetname"]
	except Exception, e:
		pass

def HouseKind(xiaoqudata):
	try:
		return u"房屋类型：", xiaoqudata["housekind"]
	except Exception, e:
		pass

def TotalBuildingArea(xiaoqudata):
	try:
		return u"建筑面积(平方米)：", xiaoqudata["totalbuildingarea"]+"\n"
	except Exception, e:
		pass


url = "http://www.shfg.gov.cn/i/wygl/xq/?id="
f = open("xiaoquinfo.txt", "wb")

def Run():
	for page_number in range(30000000,30002000):
		geturl = url + str(page_number)
		xiaoqudata = getData(geturl)
		addr = address(xiaoqudata)
		xiaoquname = name(xiaoqudata)
		wuyename = wuye(xiaoqudata)
		streetname = StreetName(xiaoqudata)
		housekind = HouseKind(xiaoqudata)
		keyid = KeyID(xiaoqudata)
		area = Area(xiaoqudata)
		totalbuildingarea = TotalBuildingArea(xiaoqudata)
		infolist = []	
		for i in keyid,xiaoquname,addr,wuyename,area,streetname,housekind,totalbuildingarea:
			if i != None:
				f.write(''.join(i)+'\n')
	f.close()
if __name__ == "__main__":
	Run()




