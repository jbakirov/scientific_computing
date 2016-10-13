def find (orig, the_str):
    a = orig.find(the_str)
    if a == -1:
        return -1;
    return a, a + len(the_str) - 1
    

myFile = open("E://sample.txt")
l = myFile.readline()
lineCount = 0
while l:
    lis = find(l, "spreading a damp chill o")
    if lis > -1:
        lineCount = lineCount + 1;
        print "Substring found at ", lis, " in line ", lineCount
    l = myFile.readline()