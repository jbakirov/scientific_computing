import csv
import re
from collections import defaultdict
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

def getUnivSalaryDict():
    nf = open("E:/documents/Roosevelt University/Scientific Computing/ds/School Data/new/SAL2014_IS/sal2014_is.csv", "r")
    
    nfilereader = csv.DictReader(nf)
    
    univSalaryDict = defaultdict(int)

    for row in nfilereader:
        univSal = parseNums(row["SAOUTLT"])      #total salary in each university
        univID = parseNums(row["UNITID"])
        arank = row["ARANK"]
        
        if not isinstance(univSal, basestring) and not isinstance(univID, basestring) and arank == "7":
            univSalaryDict[univID] = univSal
    
    nf.close()
    return univSalaryDict
    

def classwork():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    f = codecs.open("E:/documents/Roosevelt University/Scientific Computing/ds/School Data/Most-Recent-Cohorts-All-Data-Elements.csv", "r", encoding="utf-8-sig")

    filereader = csv.DictReader(f)        

    univSalDict = getUnivSalaryDict() # reads from salary data set and returns dictionary which contains ID of university and total salary
    stateFacSalary = defaultdict(int) # stores the average salary in each state    
    universityNumberInState = defaultdict(int)      #universtiy counter
    
    try:

        for row in filereader:
            
            stateName = row["STABBR"]                       #name of the state            
            highDeg = parseNums(row["HIGHDEG"])             #ID of highdeg cat/ used for 6th task            
            univID = parseNums(row["UNITID"])               #university ID
                
            ##### 6 -->>
            if not isinstance (highDeg, basestring) and not isinstance (univID, basestring) and highDeg == 4:
                stateFacSalary[stateName] += univSalDict[univID]
            universityNumberInState[stateName] +=1
            
        
        ###### 6. In each state what is the avarage salary at state 4 year institutions. [think about how we can 
        # compute this and what data we have to get the best possible answer - you must know the data files]
        
        for key, value in stateFacSalary.items():
            print "Average salary in {} is {:20,}".format(key, value/universityNumberInState[key])
        ######### --------------------------------------------------------------------------------------- >>>>>>>>>>>>>>>>>>>>>>>>>>
        

    finally:
        f.close()
        
classwork()