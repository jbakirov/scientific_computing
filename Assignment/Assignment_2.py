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
    vetpnf = defaultdict(lambda: defaultdict(int))                 #{dict:dict{}} number of veterans by state cat by public, private, for profit 
    catDict = {1 : "public", 2 : "private", 3: "for profit"}        #dict to get name of the category by ID

    try:

        for row in filereader:
            
            stateName = row["STABBR"]                       #name of the state

            numOfStudents = parseNums(row["UGDS"])          #number of students in university
            veteran = parseNums(row["VETERAN"])             #percentage of veterans
            pnf = parseNums(row["CONTROL"])                 #get ID of (public/private/for-profit)
            
            
            
            ##### 2 (a)(b)(c) -->>
            if not isinstance (numOfStudents, basestring) and not isinstance (veteran, basestring):
                vetpnf[stateName][pnf] += numOfStudents * veteran
            
        

        ###### 2. (a) Give me the number of veterans at public, private and for profit schools in each state ------------>>>>
        print "\nAnswer for 2 (a):"
        notFoundList = []
        for key, value in vetpnf.items():
            print "State: {}".format(key)
            for innerkey, val in value.items():
                try:    
                    print "    Cat: {}; Number: {}".format(catDict[innerkey], int (val))
                except:
                    notFoundList.append(innerkey)
        
        ###### 2. (b) Give me a list of states with more veterans in private schools and a list of states with more
        #veterans in public schools sorted by the magnitude of the disparity per state
        print "\nAnswer for 2 (b):"
        
        privateSchools = defaultdict(int)
        publicSchools = defaultdict(int)
        equalNumber = defaultdict(int)        

        for key, value in vetpnf.items():
            dif = abs(value[1] - value[2])      # control id = 1 - public; control id = 2 - private
            if value[1] == value[2]: equalNumber[key] = dif
            elif value[1] > value[2]: publicSchools[key] = dif
            else: privateSchools[key] = dif        

        sortedPrivate = OrderedDict(sorted(privateSchools.items(), key=lambda x: x[1]))
        sortedPublic = OrderedDict(sorted(publicSchools.items(), key=lambda x: x[1]))        
        
        print "Difference between private and public schools where number of veterans in PRIVATE schools is bigger"
        for key, value in sortedPrivate.items():
            print "State: {}; Difference: {}".format(key, value)
        
        print "Difference between private and public schools where number of veterans in PUBLIC schools is bigger"
        for key, value in  sortedPublic.items():
            print "State: {}; Difference: {}".format(key, value)

        print "Schools where equal number of veterans in PRIVATE and PUBLIC schools"
        for key, value in equalNumber.items():
            print "State: {}; Difference: {}".format(key, value) 
                           
        ###### 2. (c) Are there any states with more veterans in for-profit schools than in the other two types? If yes, list them
        print "\nAnswer for 2 (c):"
        forprofitList = []
        for key, value in vetpnf.items():        
            if value[3] > value[2] and value[3] > value[1]:
                forprofitList.append(key)
                print "State: {}; Number: {}".format(key, value[3])
        ###### ---------------------------------------------------------------------------- >>>>>>>>>>>>>>
    
        
    finally:
        f.close()
        
classwork()
#getUnivSalaryDict()