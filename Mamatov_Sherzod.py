import csv
import re

def parseNums(x):
    a = re.sub(r", (?=\d\d\d)","",x)
    try:
        x = float(a)
        x = int(a)
    except:
        pass
    return x;

def checkIfIsDigit(x):
    try:
        x.isdigit()
    except:
        return True
    return False

def calculateTheAverageRate():
    f = open("E:/documents/Roosevelt University/Scientific Computing/ds/School Data/MERGED2014_15_PP.csv", "r")
    
    applicants = {}
    students = {}
    
    try:
        filereader = csv.DictReader(f)
        
        for row in filereader:
            if row["STABBR"] is not None:
                numberOfStudentsInt = parseNums(row["UGDS"])
                admitionRateFloat = parseNums(row["ADM_RATE"])
                
                if applicants.get(row["STABBR"]) <> None and students.get(row["STABBR"]) <> None:
                    if checkIfIsDigit(numberOfStudentsInt) and checkIfIsDigit(admitionRateFloat):
                        if admitionRateFloat > 0:
                            applicants.update({row["STABBR"]:(applicants.get(row["STABBR"])+numberOfStudentsInt/admitionRateFloat)})
                            students.update({row["STABBR"]:(students.get(row["STABBR"])+numberOfStudentsInt)})                       
                else:
                    if checkIfIsDigit(numberOfStudentsInt) and checkIfIsDigit(admitionRateFloat):
                        if admitionRateFloat > 0:
                            applicants[row["STABBR"]] = numberOfStudentsInt/admitionRateFloat
                            students[row["STABBR"]] = numberOfStudentsInt                       
                                                                                                      
    finally:
        f.close()        
    
    for key in applicants.keys():
        print "State {} average rate is {}".format(key, students[key] / applicants[key])
    
calculateTheAverageRate()
