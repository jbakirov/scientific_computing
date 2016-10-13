file = open("E:/sample.txt")
line = file.readline()
while line:
    if "was bullied into taking" in line:
        print(line)
    line = file.readline()
file.close()