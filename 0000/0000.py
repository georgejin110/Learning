#!/usr/bin/env python
#-*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont

def add_number(FilePath,num,count,size):
	im = Image.open(FilePath)
	draw = ImageDraw.Draw(im)
	pic_size = im.size
	# fontsize = pic_size[0]/10
	font = ImageFont.truetype(font='Arial.ttf', size=size)
	draw.text(xy=(pic_size[0]-size*(count-0.5), 0), text=str(num), font=font, fill="red")
	im.save('avatar-new.jpg')
	im.show()

FilePath = raw_input("Input your file path: ")
num = raw_input("Input a number which you want: ")
size = int(raw_input("Input a number size which you want: "))
count = len(num)

if __name__ == '__main__':
	add_number(FilePath,num,count,size)
	