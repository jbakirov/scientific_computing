import csv
import re
from collections import defaultdict
from collections import OrderedDict
import codecs
import sys
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

def classwork():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    f = codecs.open("E:/documents/Roosevelt University/Scientific Computing/ds/School Data/Most-Recent-Cohorts-All-Data-Elements.csv", "r", encoding="utf-8-sig")

    filereader = csv.DictReader(f)
    stateDegree = defaultdict(lambda: defaultdict(int))
    try:

        for row in filereader:
            stateName = row["STABBR"]                       #name of the state
            numOfStudents = parseNums(row["UGDS"])          #number of students in university
                
            ##### 5 -->>
            for i in range(1, 55):
                cname = "PCIP"
                if i < 10: cname = cname + "0" + str(i)
                else: cname = cname + str(i)
                try:
                    r = parseNums(row[cname])
                    if not isinstance (r, basestring):
                        stateDegree[stateName][cname] += r * numOfStudents
                except: continue
        
        
        ###### 5. What are the 3 most common degrees in each state?
        degDict = getDegreeName()
        for key, value in stateDegree.items():
            ordered = OrderedDict(sorted(value.items(), key=lambda x: x[1], reverse = True))
            orderedKeys = ordered.keys()
            orderedValues = ordered.values()
            
            j = 0
            if len(ordered) > 3: j = 3
            else: j = len(ordered)
            
            print "State: {}".format(key)
            for i in range(0, j):                
                print "    {}: {} - {}".format(i+1, degDict[orderedKeys[i]], int(orderedValues[i]))
        ########## -------------------------------------------------------------------------- >>>>>>>>>>>>>>>>>>>>>.
        
        
    finally:
        f.close()
        
classwork()