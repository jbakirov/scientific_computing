import csv
import re
from collections import defaultdict
from collections import OrderedDict
import operator
import numpy as np
import matplotlib.pyplot as plt

def parseNums(x):
    a = re.sub(r", (?=\d\d\d)","",x)
    try:
        x = float(a)
        x = int(a)
    except:
        pass
    return x


def homework():
    f = open("E:/documents/Roosevelt University/Scientific Computing/ds/School Data/MERGED2014_15_PP.csv", "r")
    
    numberOfApplicants = defaultdict(int)
    numberOfUGDSInEachState = defaultdict(int)
    
    try:
        filereader = csv.DictReader(f)
        
        for row in filereader:
            if row["INSTNM"] is not None and row["STABBR"] is not None:
                v = row["STABBR"].upper() #states column
                ugds_n = parseNums(row["UGDS"])
                adm_rate = parseNums(row["ADM_RATE"])
                
                if not isinstance(ugds_n, basestring) and not isinstance(adm_rate, basestring):                    
                    #calculating the number of applicants in each state
                    if adm_rate != 0:
                        numberOfApplicants[v] += ugds_n / adm_rate
                        numberOfUGDSInEachState[v] += ugds_n
                                                                                                
    finally:
        f.close()        
    
    for key, value in numberOfApplicants.items():
        numberOfApplicants[key] = numberOfUGDSInEachState[key] / numberOfApplicants[key]
        print "State: {} has an average rate of {}".format(key, numberOfApplicants[key])

    
    orderedAvg = OrderedDict(sorted(numberOfApplicants.items(), key=operator.itemgetter(1), reverse=True))

    print "Highest average rate is - State: {} rate: {}".format(orderedAvg.items()[0][0], orderedAvg.items()[0][1]) 
    
    plt.close('all')
    fig = plt.figure(figsize=(20, 20), dpi=100)
    fig.set_facecolor('w')
    plt.bar(range(len(orderedAvg)), orderedAvg.values(), width=0.3)
    plt.xticks(range(0, len(orderedAvg)), orderedAvg.keys(), rotation=90)
    plt.show()
        
homework()

#For Wednesday:
#either give this (with applicants) 
#own name on python file

#http://matplotlib.org/api/pyplot_api.html