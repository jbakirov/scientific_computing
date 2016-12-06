import csv
import re
from collections import defaultdict
from collections import OrderedDict
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

def classwork(N):   #number of the most common degrees in 4 year schools
    reload(sys)
    sys.setdefaultencoding('utf-8')
    f = codecs.open("E:/documents/Roosevelt University/Scientific Computing/ds/School Data/Most-Recent-Cohorts-All-Data-Elements.csv", "r", encoding="utf-8-sig")

    filereader = csv.DictReader(f)

    school4Degree = defaultdict(lambda: defaultdict(int))
    degDict = getDegreeName()
    mostCommonHeap = []
    try:
        
        for row in filereader:
            
            firstGenSt = parseNums(row["PAR_ED_PCT_1STGEN"])   #first generation students
            iclevel = parseNums(row["ICLEVEL"])                 #1 - 4 year inst
            inst = row["INSTNM"]                                #name of univ
            
            if not isinstance(firstGenSt, basestring) and not isinstance(iclevel, basestring) and iclevel == 1:
                for i in range(1, 55):
                    cname = "PCIP"
                    if i < 10: cname = cname + "0" + str(i)
                    else: cname = cname + str(i)
                    try:
                        r = parseNums(row[cname])
                        if not isinstance (r, basestring): 
                            if r > 0:
                                school4Degree[inst][cname] = r
                    except: continue
                
                heappush(mostCommonHeap, (-firstGenSt, inst))
            
        ### 8. What is the most common degrees in 4 year schools with the most first generation students?
         
        for i in range(N):
            v = heappop(mostCommonHeap)
            print "School {}: {}".format(v[1], -v[0])
            j = 0
            for k, val in school4Degree[v[1]].items():
                print "   {}. {} - {}".format(j+1, degDict[k], val)
                j += 1                       

        
    finally:
        f.close()
        
classwork(4)