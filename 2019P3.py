
#Open file
f = open("periods.dat", "r")

#Get the number of sentences
strNum = f.readline()
intNum = int(strNum)

#Loop through the sentences
for i in range(0, intNum):
    # read the next line in the file and 
    # remove the carriage return at end (using .strip())
    strLine = f.readline().strip()

    # if there is a period in strLine
    if "." in strLine:
        # print strLine
        print(str(strLine))
    else:  # if there is no period in strLine
        # print strLine and add a period at the end.
        print(str(strLine) + ".")