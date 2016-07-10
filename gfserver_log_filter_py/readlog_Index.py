import re
 
#file = open("server.log")
file = open("gfserver.log")
output = open('gfserver_Index.log', 'w')
print "Truncating the file:%r !" %("gfserver_Index.log")
output.truncate()
patternall = re.compile('^.*Query Executed')
pattern=re.compile('^.*Query Executed in [0-9]{1,2}\.[0-9]* ms.*indexesUsed\([^0]\).*')
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
print "total:%d query,  index query: %d" %(totalnum,matchnum )
output.close()