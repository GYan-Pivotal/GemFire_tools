#!/usr/bin/python
#coding:utf-8
# File: readlog.py

import re
 
#file = open("server.log")
file = open("gfserver.log")
output = open('gfserver_longTime.log', 'w')
print "Truncating the file:%r !" %("longTime_s41.log")
output.truncate()
patternall = re.compile('^.*Query Executed')
pattern=re.compile('^.*Query Executed in [0-9]{3,10}\.[0-9]* ms.*')
totalnum = 0
matchnum=0
for line in file.xreadlines():
    #matched=pattern.match(line)
    #print  "%r %r" %(matched ,line)
    if patternall.match(line):
    	totalnum+=1
    	if pattern.match(line):
	        output.write(line)
	        output.write("\n")
	        matchnum+=1
    pass # do something
print "total:%d query,  longtime query: %d" %(totalnum,matchnum )
output.close()