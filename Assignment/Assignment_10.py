import csv
import re
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

    
def createFile(x):
    if x == 10:
        return open("E:/10.csv", 'wb')
    return open("E:/11.csv", 'wb')


def classwork():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    f = codecs.open("E:/documents/Roosevelt University/Scientific Computing/ds/School Data/Most-Recent-Cohorts-All-Data-Elements.csv", "r", encoding="utf-8-sig")

    filereader = csv.DictReader(f)

    try:
        data_out = createFile(10)
        dw = csv.DictWriter(data_out, delimiter=',', quoting = csv.QUOTE_MINIMAL, fieldnames = filereader.fieldnames)          # this line for assignment # 10
        dw.writer.writerow(dw.fieldnames)

        for row in filereader:        
            iclevel = parseNums(row["ICLEVEL"])             #level of institution
            
            ##### 10 -->>
            if not isinstance(iclevel, basestring) and iclevel == 1:
                dw.writerow(row)
        
        
        ###### 10. create a new file to contain only rows for four year colleges
        print "Done"
        data_out.close()
        
    finally:
        f.close()
        
classwork()