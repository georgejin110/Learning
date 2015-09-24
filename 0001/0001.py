#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random, string, sys

def inv_code(count,number):
	f = open("code.txt", "wb")
	chars = string.digits + string.uppercase
	i = 0
	while i < count:
		s = [random.choice(chars) for n in range(number)]
		f.write(''.join(s) + '\n')
		i += 1

def Run():
	arg1, arg2 = sys.argv[1], sys.argv[2]
	try:
		arg1, arg2 = int(arg1), int(arg2)
	except ValueError, e:
		print arg1, arg2+' are strings.', e
		print "Please input two NUMBERS."
	if len(sys.argv)!=3:
		print "Error! 2 argument required.", "("+str(len(sys.argv)), "given)."

	inv_code(arg1, arg2)
	

if __name__ == '__main__':
	Run()
	

# print inv_code(10)



