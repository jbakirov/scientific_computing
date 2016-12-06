import operator
import csv
import re
from collections import defaultdict
from collections import OrderedDict
import codecs
import sys


def parseNums(x):
    a = re.sub(r", (?=\d\d\d)","",x)
    try:
        x = float(a)
        x = int(a)
    except:
        pass
    return x
    

def classwork():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    f = codecs.open("E:/documents/Roosevelt University/Scientific Computing/ds/School Data/Most-Recent-Cohorts-All-Data-Elements.csv", "r", encoding="utf-8-sig")

    filereader = csv.DictReader(f)
    stateNumDict = defaultdict(int)                                #total number of engineers by state

    try:
        for row in filereader:
            
            stateName = row["STABBR"]                       #name of the state
            numOfEng = parseNums(row["OVERALL_YR4_N"])      #total number of engineer students
            percentage = parseNums(row["PCIP14"])           #percentage of engineer students who graduated
        
            
            
            if not isinstance (numOfEng, basestring) and not isinstance (percentage, basestring):
                fnumber = numOfEng * percentage / 100
                stateNumDict[stateName] += fnumber
            
        
        ##### 1. Which state create the most engineers? ---------->>>
        sortedByVal = OrderedDict(sorted(stateNumDict.items(), key=operator.itemgetter(1), reverse=True))        
        print next(iter(sortedByVal.items()))

    finally:
        f.close()
        
classwork()