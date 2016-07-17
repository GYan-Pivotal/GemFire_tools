
import datetime
import os
import sys

def main(argv):
    targetFile=argv[1]
    outputFile=argv[2]
    
    dateStart = datetime.date(2016, 4, 26)
    tStart = datetime.time(4,40)
    dtStart=datetime.datetime.combine(dateStart, tStart)
    
    dateEnd = datetime.date(2016, 4, 27)
    tEnd= datetime.time(2,0)
    dtEnd=datetime.datetime.combine(dateEnd, tEnd)
    
    dateInit = dtStart
    for i in range((dtEnd - dtStart).seconds):
        day = dtStart + datetime.timedelta(seconds=i)
        if (i%60 == 0):
            strDateFrom= dateInit.strftime( '%Y/%m/%d %H:%M:%S' )+".000 CST"
            strDate= day.strftime( '%Y/%m/%d %H:%M:%S' )+".000 CST"
            #print 'gemfire stats -starttime="'+strDateFrom+'" -endtime="'+strDate+'" -archive=statics_p.gfs|grep cpuActive >> aa.txt'
            os.system('gemfire stats -starttime="'+strDateFrom+'" -endtime="'+strDate+'" -archive='+targetFile+'|grep cpuActive >>'+outputFile)
            dateInit=day
            #print strDate


if __name__ == '__main__':
    main(sys.argv)
