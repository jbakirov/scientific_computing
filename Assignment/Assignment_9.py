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
    
    completionRate = defaultdict(lambda: defaultdict(int)) #completion rate : {stateName: {categoryID: number}}
    numOfSchEachType = defaultdict(lambda: defaultdict(int)) #number of schools in each state by cat {state:{categoryID:+1}}
            
    try:
        for row in filereader:
            
            stateName = row["STABBR"]                       #name of the state
            pnf = parseNums(row["CONTROL"])                 #get ID of (public/private/for-profit)            
            c100_4 = parseNums (row["C100_4"])              #completion rate                    
                    
            ##### 9 -->>
            if not isinstance(pnf, basestring) and not isinstance(c100_4, basestring):
                completionRate[stateName][pnf] += c100_4;
                numOfSchEachType[stateName][pnf] += 1;
            
        
        ###### 9. What is the average completion rate C100_4 for students in priv, pub and for-profit schools
        # in each state? (CONTROL)

        for key, val in completionRate.items():
            print "{}".format(key)
            i = 0
            for k, v in val.items():
                print "    {}. {} : {}".format(i+1, catDict[k], v/numOfSchEachType[key][k])
                i += 1
        ######## ------------------------------------------------------------------------------------------ >>>>>>>>>>>>>>>>>>>>
                
    finally:
        f.close()
        
classwork()