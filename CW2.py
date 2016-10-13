import re
import csv

def parseNums(x):
    a = re.sub(r", (?=\d\d\d)","",x)
    try:
        x = float(a)
        x = int(a)
    except:
        pass
    return x

def Show(x):
    print x[1], "found at location ", x[0], "in line", x[2]
    
counter = 0

def parse(x):
        if x.isdigit():
            return int(x)
        return 0

for LineNumber, line in enumerate (open("E:/documents/Roosevelt University/Scientific Computing/ds/csv.csv", "r")):
    #[Show((i, x, LineNumber)) for i,x in enumerate(line.split()) if x == "there"]
    Columns = line.split(";")
    if Columns[2] <> "numEmps":
        if Columns[4] == "Scottsdale":
            counter = counter + parseNums(Columns[2])
        #print line

print(counter)


def usingCSVModule():
    #with open("E:/documents/Roosevelt University/Scientific Computing/ds/csv.csv", "r") as csvfile:
    f = open("E:/documents/Roosevelt University/Scientific Computing/ds/csv.csv", "r")
    counter = 0;
    try:
        filereader = csv.reader(f, delimiter = ';')
        for row in filereader:
            #Columns = row.split(";")
            if row[2] <> "numEps":
                if row[4] == "Scottsdale":
                    counter = counter + parseNums(row[2])
    finally:
        f.close()
    
    
usingCSVModule()