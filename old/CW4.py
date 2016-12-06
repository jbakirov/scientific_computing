import csv
import re
from collections import defaultdict
from collections import OrderedDict
import operator

def parseNums(x):
    a = re.sub(r", (?=\d\d\d)","",x)
    try:
        x = float(a)
        x = int(a)
    except:
        pass
    return x


def usingCSVModule():
    #with open("E:/documents/Roosevelt University/Scientific Computing/ds/csv.csv", "r") as csvfile:
    f = open("E:/documents/Roosevelt University/Scientific Computing/ds/csv.csv", "r")
    counter = 0;
    try:
        filereader = csv.reader(f, delimiter = ';')
        for row in filereader:
            print row
            if row[2] <> "numEps":
                if row[4] == "Scottsdale":
                    counter = counter + parseNums(row[2])
    finally:
        f.close()
    print(counter)
    
#usingCSVModule()


#number of students 'UGDS'


#1. How many schools are in Delaware? 
#2. Using dictionary tell how many schools are in each state?
#3. Which state has the highest total percentage of students whose parents level of education is high school?


def homework():
    f = open("E:/documents/Roosevelt University/Scientific Computing/ds/School Data/MERGED2014_15_PP.csv", "r")
    stateDict = defaultdict(int)
    percentDict = defaultdict(float)
    totalNumberOfStudents = 0
    totalPC = 0
    
    numberOfSchools = defaultdict(int)
    avgAdm = defaultdict(float)
    
    try:
        filereader = csv.DictReader(f)
        
        for row in filereader:
            if row["INSTNM"] is not None and row["STABBR"] is not None:
                v = row["STABBR"].upper()
                stateDict[v] += 1
                f_perc = parseNums(row["PAR_ED_PCT_HS"])
                ugds_n = parseNums(row["UGDS"])
                adm_rate = parseNums(row["ADM_RATE"])
                
                if not isinstance(ugds_n, basestring):
                    totalNumberOfStudents += ugds_n
                    if not isinstance(f_perc, basestring):
                        percentDict[v] += f_perc * ugds_n
                        totalPC += f_perc * ugds_n        
                    if not isinstance(adm_rate, basestring):
                        avgAdm[v] += adm_rate
                        numberOfSchools[v] += 1
                                                                
    finally:
        f.close()    

    print "There are {} schools in Delaware".format(stateDict["DE"])
    
    
    #stateSDesc = OrderedDict(sorted(stateDict.items(), key=operator.itemgetter(1), reverse=True))                
    #for key, value in stateSDesc.items():
    #    print "There are {} schools in {}".format(value, key)
        
    #d_desce = OrderedDict(sorted(percentDict.items(), key=operator.itemgetter(1), reverse=True))
    
    #items = d_desce.items()
    #for x in range(0, 3):
    #    print "State: {} ; Percentage: {} %".format(items[x][0], items[x][1] * 100 / totalNumberOfStudents)
    
    for key, value in avgAdm.items():
        avgAdm[key] = value/numberOfSchools[key]
        print "State: {}; AvgPercentage: {}".format(key, value/numberOfSchools[key])

    print "Highest is : {}".format(max(avgAdm.iteritems(), key=operator.itemgetter(1)))
    
    #print totalPC
    #print max(percentDict.iteritems(), key=operator.itemgetter(1))[1] * 100 / totalPC
    
    

        
homework()
