#!/home/tarun/anaconda2/bin/python
# coding: utf-8

from PIL import Image
import math

#File to read the contents from
filename = "input.txt"

#Image name to save image to
outputfile = "tarun.png"

#Image Dimensions
imageSize = (512,512)

#Max Address Size(depends on resolution of screen). In this case = log2(512)
resolution = math.log(imageSize[0],2)

#Image to draw pixels
image = Image.new("L", imageSize)

#Defining sets of vowels etc.
vowels = ['a','e','i','o','u']
glides = ['y','w']
liquids = ['l','r']
nasals = ['m','n']

#Remove Non-Ascii Characters
def remove_non_ascii(text):
	return ''.join(i.strip() for i in text if ord(i)<128)

#Characters to corresponding bins
def phon(c):
	if c in vowels:
		return 1
	if c in glides:
		return 2
	if c in liquids or c in nasals:
		return 3
	return 4

#Applying Transformation to point(pixel)
def trans(c,loc):
	(x,y) = loc
	if c==1:
		return (x/2 , y/2)
	if c==2:
		return ((x+512)/2 , y/2)
	if c==3:
		return (x/2 , (y+512)/2)
	return ((x+512)/2 , (y+512)/2)

#Function that takes line in reverse order and apply corresponding transformation
def text_to_fractal(s,loc):
	if len(s)<resolution:
		return loc
	i = 0
	while i != resolution:
		loc = trans(phon(s[i]),loc)
		i+=1
	image.putpixel(loc, 255)
	# print loc
	for i in range(9,len(s)):
		if s[i] == ' ':
			continue
		loc = trans(phon(s[i]),loc)
		image.putpixel(loc, 255)
		print loc
	return loc

#Read contents of file
with open(filename) as f:
	content = f.readlines()

#Reverse the order of lines
content = content[::-1]

#Default location is (0,0)
loc = (0,0)
#for loop that calls text_to_fractal function with the reversed line
for line in content:
	loc = text_to_fractal(line[::-1],loc)
#Save and show Image
image.save(outputfile)
image.show()