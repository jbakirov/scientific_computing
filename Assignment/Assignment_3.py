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



def classwork():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    f = codecs.open("E:/documents/Roosevelt University/Scientific Computing/ds/School Data/Most-Recent-Cohorts-All-Data-Elements.csv", "r", encoding="utf-8-sig")

    filereader = csv.DictReader(f)
    catDict = {1 : "public", 2 : "private", 3: "for profit"}        #dict to get name of the category by ID
    povertyRateDict = defaultdict(lambda: defaultdict(int))         #number of poverty rate students by state at private, public and for profit schools
    stateStudents = defaultdict(int)                                #total number of students in each state
    
    try:

        for row in filereader:
            
            stateName = row["STABBR"]                       #name of the state
            numOfStudents = parseNums(row["UGDS"])          #number of students in university
            pnf = parseNums(row["CONTROL"])                 #get ID of (public/private/for-profit)
            povertyRate = parseNums(row["POVERTY_RATE"])    #poverty rate column
                                
                        
            #### 3 (a) -->>
            if not isinstance (numOfStudents, basestring) and not isinstance (povertyRate, basestring):
                povertyRateDict[stateName][pnf] += numOfStudents * povertyRate / 100
                stateStudents[stateName] += numOfStudents
                   
        
        ###### 3. For four year, mostly bachelors degree colleges: 
        print "\n(a) Number of poverty rate students at private, public and for profit schools:"
        for key, value in povertyRateDict.items():
            print "State: {}".format(key)
            for innerkey, val in value.items(): 
                print "    Cat: {}; Number: {}".format(catDict[innerkey], int (val))
 
        print "\n(b) Percentage of poverty rate students at private, public and for profit schools:"
        for key, value in povertyRateDict.items():
            print "State: {}".format(key)
            for innerkey, val in value.items(): 
                print "    Cat: {}; Percentage: {}".format(catDict[innerkey], val/stateStudents[key] * 100)
        ##### ----------------------------------------------------------------------------- >>>>>>>>>>>>>>>
        
    finally:
        f.close()
        
classwork()