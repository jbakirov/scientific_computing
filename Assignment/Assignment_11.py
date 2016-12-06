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
    
    univSalaryDict = defaultdict(lambda: defaultdict(int))

    for row in nfilereader:
        univSal = parseNums(row["SAOUTLT"])      #total salary in each university
        univID = parseNums(row["UNITID"])
        arank = row["ARANK"]
        
        if not isinstance(univSal, basestring) and not isinstance(univID, basestring) and arank == "7":
            univSalaryDict[univID] = [univSal, arank]
            print univSal, arank
    
    nf.close()
    return univSalaryDict
    
def createFile(x, path):
    if x == 10:
        return open("E:/10.csv", 'wb')
    return open("E:/11.csv", 'wb')


def classwork():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    f = codecs.open("E:/documents/Roosevelt University/Scientific Computing/ds/School Data/Most-Recent-Cohorts-All-Data-Elements.csv", "r", encoding="utf-8-sig")

    filereader = csv.DictReader(f)            
    outCols = ["UNITID", "INSTNM", "STABBR", "OVERALL_YR4_N", "PCIP14", "UGDS", "VETERAN",
            "CONTROL", "POVERTY_RATE", "HIGHDEG", "FIRSTGEN_YR2_N", "FIRSTGEN_YR4_N",
            "ICLEVEL", "SCH_DEG", "FIRST_GEN", "PREDDEG", "C100_4", "RET_FT4", "SAOUTLT", "ARANK"]
    try:
        data_out = createFile(11)
        dw = csv.DictWriter(data_out, delimiter=',', quoting = csv.QUOTE_MINIMAL, extrasaction='ignore', fieldnames = outCols) # this line for assignment # 11
        dw.writer.writerow(dw.fieldnames)

        univSalaryDict = getUnivSalaryDict()
        
        for row in filereader:
            
            univID = parseNums(row["UNITID"])               #university ID
            
            row["SAOUTLT"] = univSalaryDict[univID][0]        
            row["ARANK"] = univSalaryDict[univID][1]
            
                        
            ##### 11 -->>
            dw.writerow(row)
        
        
        ###### 11. create a new file to contain all-of and only the rows and columns you used in questions 1-10 of this assignment
        print "Done"
        data_out.close()
        
    finally:
        f.close()
        
classwork()