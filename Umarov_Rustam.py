import pandas as pd 
schoolNumber = {}
admRate ={}
numberOfApplicants = {}
numberOfStudents = {}
def IsNumeric(x):
    try:
        int(x)
        float(x)
        return x
    except:
        return 0
df = pd.read_csv("D:/MERGED2014_15_PP.csv")
NameOfState = df.STABBR #The name of the state
AdmissionRate = df.ADM_RATE #Admission rate in %
NumberOfStudents = df.UGDS #Number of students
#Number of schools
for (i, item) in enumerate(NameOfState):
    if item<>None:
        if schoolNumber.get(item)<>None:
               schoolNumber.update({item:(schoolNumber.get(item) + 1)})      
        else:
            schoolNumber[item] = 1
#Number of applicants
for (i,rate) in enumerate(AdmissionRate):
    if IsNumeric(rate)>0 and IsNumeric(NumberOfStudents[i])>0:
        if numberOfApplicants.get(NameOfState[i])<>None:
            numberOfApplicants.update({NameOfState[i]:(numberOfApplicants.get(NameOfState[i])+NumberOfStudents[i]/rate)})
        else:
            numberOfApplicants[NameOfState[i]] = NumberOfStudents[i]/rate
#Number of students 
for (i, students) in enumerate(NumberOfStudents):
    if IsNumeric(students)>0 and IsNumeric(AdmissionRate[i])>0:
        if numberOfStudents.get(NameOfState[i])<>None:
            numberOfStudents.update({NameOfState[i]:(numberOfStudents.get(NameOfState[i]))+IsNumeric(students)})
        else:
            numberOfStudents[NameOfState[i]]=IsNumeric(students)
#Find out total admission rate
for key in numberOfApplicants.keys():
   admRate[key]=numberOfStudents[key] / numberOfApplicants[key]
#Print admission rate by state
for key, value in sorted(admRate.iteritems(), key=lambda (k,v): (v,k)):
    print "%s %s %s" % (key,"has admission rate of",value)
print "********************************", "\n", "********************************", "\n", "********************************"
#Print number of students by state
for key, value in sorted(numberOfStudents.iteritems(), key=lambda (k,v): (v,k)):
    print "%s %s %s %s" % (key,"has",value,"students")
print "********************************", "\n", "********************************", "\n", "********************************"
#Print number of applicants by state
for key, value in sorted(numberOfApplicants.iteritems(), key=lambda (k,v): (v,k)):
    print "%s %s %s %s" % (key,"had",value,"applicants")
print "********************************", "\n", "********************************", "\n", "********************************"
#Print number of schools by state
for key, value in sorted(schoolNumber.iteritems(), key=lambda (k,v): (v,k)):
    print "%s %s %s %s" % (key,"has",value,"school(s)")