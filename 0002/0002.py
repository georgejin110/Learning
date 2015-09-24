#!/usr/bin/env python
#-*- coding: utf-8 -*-

import MySQLdb

db = MySQLdb.connect("localhost","python","python","python")
cursor = db.cursor()