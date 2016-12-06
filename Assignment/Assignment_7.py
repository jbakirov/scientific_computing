import csv
import re
from collections import defaultdict
import codecs
import sys
from heapq import heappush, heappop

import pandas as pd

def parseNums(x):
    a = re.sub(r", (?=\d\d\d)","",x)
    try:
        x = float(a)
        x = int(a)
    except:
        pass
    return x

    
def getDegreeName():
    xl =  pd.ExcelFile("E:/documents/Roosevelt University/Scientific Computing/ds/School Data/CollegeScorecardDataDictionary-08-18-2016.xlsx")
    degreeDict = defaultdict(basestring)
    forDegreeDict = xl.parse("data_dictionary")
    
    colVarName = forDegreeDict["VARIABLE NAME"]
    colLabel = forDegreeDict["LABEL"]
    
    for (i, row) in enumerate(colVarName):
        try:
            if "PCIP" in row:
                degreeDict[row] = colLabel.get(i)
        except: continue

    return degreeDict

def classwork(N): #N - first N schools with highest retention rate
    reload(sys)
    sys.setdefaultencoding('utf-8')
    f = codecs.open("E:/documents/Roosevelt University/Scientific Computing/ds/School Data/Most-Recent-Cohorts-All-Data-Elements.csv", "r", encoding="utf-8-sig")

    filereader = csv.DictReader(f)    
    schDegreePr = defaultdict(lambda: defaultdict(float))           # school name - degree name - rate    
    schRetHeap = []
    notFound = []
    
    try:

        for row in filereader:
            
            inst = row["INSTNM"]                            #name of the university            
            ret = parseNums(row["RET_FT4"])                 #retention rate
                    
            ##### 7 -->>
            if not isinstance(ret, basestring):
                for i in range(1, 55):
                    cname = "PCIP"
                    if i < 10: cname = cname + "0" + str(i)
                    else: cname = cname + str(i)
                    
                    try: 
                        r = parseNums(row[cname])
                        if r > 0:
                            schDegreePr[inst][cname] = r
                    except: notFound.append(cname)
                
                if ret == 0: heappush(schRetHeap, (ret, inst))
                else: heappush(schRetHeap, (-ret, inst))
        
        
        ###### 7. What are the most common degrees at the schools with the highest retention rates, nationally?
        ###############!!!!!!!!!!!! retention rate of first 92 universities is 1
      
        degDict = getDegreeName()

        for i in range(N):
            v = heappop(schRetHeap)
            print "Retention rate in {}: {}".format(v[1], -v[0])
            j = 0
            for k, val in schDegreePr[v[1]].items():
                print "   {}. {} - {}".format(j+1, degDict[k], val)
                j += 1                       

    finally:
        f.close()
        
classwork(4)