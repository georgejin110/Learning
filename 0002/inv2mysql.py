#!/usr/bin/env python
#-*- coding: utf-8 -*-

import MySQLdb as mdb

HOST = 'localhost'
USER = 'python'
PASSWD = 'python'
DB = 'python'
CHARSET = 'utf8'

def db_connection(host=HOST,user=USER,passwd=PASSWD,db=DB,charset=CHARSET):
	return mdb.connect(host=host,user=user,passwd=passwd,db=db,charset=CHARSET)

def drop_table(table='invite_code'):
	drop = "DROP TABLE IF EXISTS %s" % table
	return cursor.execute(drop)

def create_table(table='invite_code'):
	create = '''CREATE TABLE %s (
			ID INT(1) NOT NULL,
			INVITE_CODE varchar(32) NOT NULL)''' % table
	return cursor.execute(create)

def codelist():
	invite_code_file = open('../0001/code.txt', 'r')
	codelist = map(lambda x: x.rstrip("\n"), invite_code_file.readlines())
	return codelist
			

def insertcode(table='invite_code'):
	drop_table(table)
	create_table(table)
	codes = codelist()
	for i in codes:
		query = "INSERT INTO %s (%s) VALUES ('%s')" % (table, 'INVITE_CODE', i)
		cursor.execute(query)
		db.commit()
	db.close()

db = db_connection()
cursor = db.cursor()
# newID = cursor.lastrowid
insertcode()
