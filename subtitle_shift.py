import os
import sys
import fileinput

#Put the .srt filename here:
filename='Kabhi Khushi Kabhie Gham... Sometimes Happiness Sometimes Sorrow  (2001).BDRip.en.srt'

#Decide how much you want to shift, and then execute (in the same directory as the .srt file)
shift = -1

with open(filename) as f:
    content = f.readlines()

for i in range(0,len(content)):
	for j in range(8,len(content[i])-2):
		if content[i][j] == ',' and content[i][j-3] == ':':
			time = int(content[i][j-2:j])+int(content[i][j-5:j-3])*60+int(content[i][j-8:j-6])*3600
			time += shift
			content[i] = content[i][0:j-8]+"{0:0=2d}".format(time/3600)+":"+"{0:0=2d}".format(time%3600/60)+":"+"{0:0=2d}".format(time%60)+content[i][j:]

fo = open(filename, "rw+")
for item in content:
	fo.write("%s" % item)
