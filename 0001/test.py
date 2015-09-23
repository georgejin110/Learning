#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys

def test():

	if isinstance(int(sys.argv[1]), int) is True:
		print sys.argv[1] + ' is a int.'
	else:
		print sys.argv[1] + ' is not a int.'
		print type(sys.argv[1])	

if __name__ == '__main__':
	test()