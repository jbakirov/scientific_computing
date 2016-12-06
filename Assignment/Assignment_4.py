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

    state_fy_y2 = defaultdict(int) #number of first year generation go to 2 year college    
    state_fy_y4 = defaultdict(int) #number of first year generation go to 4 year college
        
    
    try:

        for row in filereader:
    
            stateName = row["STABBR"]                       #name of the state
            firstGen_yr2 = parseNums(row["FIRSTGEN_YR2_N"]) #first generation year 2
            firstGen_yr4 = parseNums(row["FIRSTGEN_YR4_N"]) #first generation year 4
            
            #### 4 -->>
            if not isinstance (firstGen_yr2, basestring) and not isinstance(firstGen_yr4, basestring):
                state_fy_y2[stateName] += firstGen_yr2
                state_fy_y4[stateName] += firstGen_yr4
            
        
        ###### 4. In each state, do more first generation students go to two year or four year colleges?
        for key, value in state_fy_y2.items():
            print "State: {}".format(key)
            if state_fy_y4[key] > value: print "    4 year colleges: {} (# of students)".format(state_fy_y4[key])
            else: print "    2 year colleges: {} (# of students)".format(value)
            print "--------------------------------"

        ######### -------------------------------------------------------------------------- >>>>>>>>>>>>>>
                
    finally:
        f.close()
        
classwork()